import boto3

# For securityGroups

client = boto3.client('ec2')
response = client.describe_security_groups()
print(response)
print('securityGroups')
print('--------------\n')
for securityGroups in response['SecurityGroups']:
    print(f"{securityGroups['GroupName']}       \t{securityGroups['GroupId']}")

# For Subnets

ec2_client = boto3.client('ec2')
print('\nSubnets:')
print('-------\n')
sn_all = ec2_client.describe_subnets()
print(sn_all)
for sn in sn_all['Subnets'] :
    print(sn['SubnetId'])

# For KeyPairs

print('\nKey-Pairs')
print('----------\n')
kp_all = ec2_client.describe_key_pairs()
for kp in kp_all['KeyPairs']:
    print(kp['KeyName'])

# For InstanceTypeOfferings

print('\nInstanceTypeOfferings')
print('-----------------------\n')
type_offerings = ec2_client.describe_instance_type_offerings()
for type in type_offerings["InstanceTypeOfferings"]:
    print(type['InstanceType'])

# For Images with Respective Names

# print('\nSelect Instance Type')
# print('-----------------------')
# names = ec2_client.describe_

# str1 = '''Installing Amazon CLI
#             Configuring AWS CLI Tools
#             List All AvailabilityZone
#             Launch an Instance
#             Attach A Volume
#             Create S3 Bucket
#             Attach CloudFront Storage
#             List All Instances
#             List All KeyPairs
#             List All SecurityGroups
#             List All Subnets
#             List All InstanceTypeOfferings
#             List All Volume
#             List All VolumeOffering'''
