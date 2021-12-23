import boto3
from secrets import access_key, secret_access_key, bucket_name
import os

from botocore import response

client = boto3.client('lambda', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

# with open('lambda.zip', 'rb') as f:
#     zipped_code = f.read()
# ####### Create function #########
# response = client.create_function(
#     Code = dict(ZipFile = zipped_code),
#     FunctionName = 'testfunction',
#     Runtime = 'python3.9',
#     Role = 'arn:aws:iam::870626234162:role/lambda_test',
#     Handler = 'handler.lambda_handler',
#     Timeout = 300,
#     Publish = True
# )

##### Delete lambda function ########
# response = client.delete_function(FunctionName="testfunction")
##### Get all functions ###########
response = client.list_functions()
f_arn = response['Functions'][0]['FunctionArn']
print(f_arn)
