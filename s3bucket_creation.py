import boto3
from secrets import access_key, secret_access_key

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)
client.create_bucket(Bucket = "youtubedatabucket")
print('Bucket created....')