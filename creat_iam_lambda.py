import boto3
import json

iam = boto3.client('iam')
role_policy = {
    "Version": "2021-12-20",
    "Statement": [
        {
            "Effects": "Allow", 
            "Action": [
                "s3:ListBucket"
            ],

        },
        {
            "Effects": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::youtubedatabucket/*"
            ]
        }
    ]
}


response = iam.create_role(RoleName = 'LambdaFristTest', AssumeRolePolicyDocument = json.dumps(role_policy))
print("Response:::: ", response)