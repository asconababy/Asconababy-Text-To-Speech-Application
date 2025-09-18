import AWS from "aws-sdk";

const polly = new AWS.Polly();

export const handler = async (event) => {
  const text = event.text || "Hello from AWS Polly!";
  
  const params = {
    Text: text,
    OutputFormat: "mp3",
    VoiceId: "Joanna"
  };

  const result = await polly.synthesizeSpeech(params).promise();

  return {
    statusCode: 200,
    headers: { "Content-Type": "audio/mpeg" },
    body: result.AudioStream.toString("base64"),
    isBase64Encoded: true
  };
};
