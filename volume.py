import boto3
ec2_client = boto3.client('ec2')

# List All Volumes Storage
print('Volumes Details')
print('----------------')
print(f"AvailabilityZone  \t\tVolumeId  \t\t\t\tName")
volumes_all = ec2_client.describe_volumes()
for vol in volumes_all["Volumes"]:
    print(f'{vol["AvailabilityZone"]}  \t\t{vol["VolumeId"]}  \t\t{vol["Tags"][0]["Value"]}')

# List All Volumes Offering
print('\n\nAll Available Volumes Types')
print("----------------------------")
print('''
gp2 - General Purpose (SSD)
io1 - Provisioned IOPS (SSD)
io2 - Provisioned IOPS (SSD)
sc1 - Cold HDD
st1 - Throughput Optimized hard disk drive (HDD)
Magnetic (standard)
''')