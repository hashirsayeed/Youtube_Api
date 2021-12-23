import json
import boto3
from mypy_boto3_s3.type_defs import _RequiredRoutingRuleTypeDef
def lambda_handler(event, context):
    # aws_access_key = event['access_key']
    # aws_secret_key = event['secret_access_key']
    # bucket_name = event['bucket']
    # fl_name = event['File']
    # client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    # files = client.list_objects(Bucket = bucket_name)['Contents']
    # if files[0]['Key'] == fl_name:
    #     return{
    #         'statusCode': 200,
    #         'body': json.dumps('Hello Hash')
    #     }
    # else:
    #     return{
    #         'statusCode': 404,
    #         'body': json.dumps('Not found...')
    #     }
    return {
        'statusCode': 200,
        'body': json.dumps('Invoked')
    }