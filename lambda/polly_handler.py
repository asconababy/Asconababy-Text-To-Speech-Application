import json
import boto3
import uuid
import os
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

polly = boto3.client('polly')
s3 = boto3.client('s3')

BUCKET_NAME = os.environ.get("BUCKET_NAME", "your-fallback-bucket-name")

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    logger.info(f"Bucket name: {BUCKET_NAME}")
    method = event.get("requestContext", {}).get("http", {}).get("method")

    # Handle CORS preflight request
    if method == "OPTIONS":
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            'body': ''
        }

    try:
        logger.info("Processing request...")
        body = json.loads(event.get('body', '{}'))
        text = body.get('text')
        logger.info(f"Text to convert: {text}")

        if not text:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*'
                },
                'body': json.dumps({'error': 'Text is required'})
            }

        # Call Amazon Polly
        logger.info("Calling Polly...")
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )
        logger.info("Polly synthesis completed")

        audio_stream = response['AudioStream'].read()
        filename = f"polly-{uuid.uuid4().hex}.mp3"

        # Upload to S3
        logger.info(f"Uploading to S3 bucket: {BUCKET_NAME}")
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=audio_stream,
            ContentType='audio/mpeg'
        )
        logger.info("S3 upload completed")

        # Generate presigned URL
        presigned_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET_NAME, 'Key': filename},
            ExpiresIn=3600
        )

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*'
            },
            'body': json.dumps({'url': presigned_url})
        }

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*'
            },
            'body': json.dumps({'error': str(e)})
        }