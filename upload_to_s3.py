import boto3
from secrets import access_key, secret_access_key, bucket_name
import os

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)
####### upload file ##############
for file in os.listdir():
    if 'json' in file:
        client.upload_file(file, bucket_name, str(file))
        print('upload done..')
        break

########## delete file #############
fl_name = "fightincowboy.json"
files = client.list_objects(Bucket = bucket_name)['Contents']
if files[0]['Key'] == fl_name:
    client.delete_object(Bucket = bucket_name, Key = fl_name)
    print('Deleted...')