import boto3
client = boto3.client("ec2")


response = client.start_instances(
    InstanceIds=[
        'i-045a754bb6ea65723',
    ]
)