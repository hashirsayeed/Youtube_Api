import boto3 
import json
from secrets import access_key, secret_access_key, ami

from botocore import response

### get private key if ket is already created
def ec2_private_key():
    with open('ec2.txt', 'r') as f:
        lines = f.readlines()
    text = ""
    for l in lines:
        l = l.split('\\')[0]
        text += l
    return text


ec2 = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

#####create key-pair
# key_pair = ec2.create_key_pair(KeyName='ec2-key-pair')

# private_key = key_pair["KeyMaterial"]
# private_key = private_key[32:-31]

# with open('ec2.txt', 'w') as f:
#     f.write(private_key)

# #####delete key-pair
# response = ec2.delete_key_pair(KeyName='ec2-key-pair')
# print(response)

#### get all key pairs 
# response = ec2.describe_key_pairs()
# print(response)

######CREATE EC2 instance
# instance = ec2.run_instances(
#     ImageId=ami,
#     MinCount=1,
#     MaxCount=1,
#     InstanceType="a1.medium",
#     KeyName='ec2-key-pair'
# )
# print(instance['Instances'][0]['InstanceId'])

#### start instance
# response = ec2.start_instances(InstanceIds=['i-0041e8f73228915d9'])
# print(response)

######get instances
# response = ec2.describe_instances()
# print(response['Reservations'][0]['Instances'][0]['Monitoring']['State'])

###### Stop instance
# response = ec2.stop_instances(InstanceIds=['i-0041e8f73228915d9'])
# print(response)

#####terminate instance
# response = ec2.terminate_instances(InstanceIds=['i-0041e8f73228915d9'])
# print(response)

####delete instance
# response = ec2.delete_instances(InstanceIds=['i-0041e8f73228915d9'])