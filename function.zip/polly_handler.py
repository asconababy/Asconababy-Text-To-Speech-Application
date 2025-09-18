import boto3
import json
import os

polly = boto3.client("polly")
s3 = boto3.client("s3")
bucket_name = os.environ["BUCKET_NAME"]

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        text = body.get("text", "Hello from AWS Polly!")
        voice_id = body.get("voiceId", "Joanna")

        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId=voice_id
        )

        audio_stream = response["AudioStream"].read()
        key = f"speech-{context.aws_request_id}.mp3"

        s3.put_object(Bucket=bucket_name, Key=key, Body=audio_stream)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Success",
                "file": f"s3://{bucket_name}/{key}"
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
