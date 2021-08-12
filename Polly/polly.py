import boto3
from datetime import datetime
from botocore.exceptions import ClientError
import logging

#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.start_speech_synthesis_task
pollyClient = boto3.client('polly', region_name = "us-east-1")
#sample Input Text to convert to Speech
sampleText = "This is some sample text that we will be playing as speech with Amazon Polly"


audioBucket = "sample-bucket-polly-mars"
now = datetime.now() #Timestamps to give keynames for objects we push to S3
current_time = now.strftime("%H:%M:%S")

#start speech synthesis task
response = pollyClient.start_speech_synthesis_task(
        LanguageCode = 'en-US',
        OutputFormat = 'mp3',
        OutputS3BucketName = audioBucket,
        OutputS3KeyPrefix= "InputAudio" + current_time,
        Text = sampleText,
        VoiceId = 'Brian')

#Find the key to send to pre-signed URL
object_name = response['SynthesisTask']['OutputUri'] #returns entire S3 Path, need to index for key to create S3 Pre-Signed URL
startIndex = object_name.find("InputAudio") 
keyName = object_name[startIndex: len(object_name)]
print(keyName)

#S3 Client to get pre-signed URL
#Pre-Signed URL: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html#:~:text=A%20presigned%20URL%20is%20generated,user%20who%20generated%20the%20URL.
s3_client = boto3.client('s3')


def create_presigned_url(bucket_name, object_name, expiration=3600):
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                            ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    
    return response


audioFile = create_presigned_url(audioBucket, keyName)
print(audioFile)