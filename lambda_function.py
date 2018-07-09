import boto3
import urllib
def lambda_handler(event, context):
    s3 = boto3.client("s3")
    if event:
        file_obj = event["Records"][0]
        filename = str(file_obj['s3']['object']['key'])
        filename = urllib.parse.unquote_plus(filename)
        fileObj = s3.get_object(Bucket = "aws-s3-upload-bucket", Key="upload/Greetings.txt")
        file_content = fileObj["Body"].read().decode('utf-8')
        print("File Content: ", file_content)
        print("File Name: ", str(file_obj['s3']['object']['key']))
        print("File Size: ", str(file_obj['s3']['object']['size']), "Bytes")
        print("Number of words in the text file: ",len(file_content.split()))
        print("File location in S3: ", str(file_obj['s3']['bucket']['name']),"/",str(file_obj['s3']['object']['key']))
