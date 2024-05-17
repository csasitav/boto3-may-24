import boto3
ec2 = boto3.client("ec2")

response = ec2.stop_instances(
    InstanceIds=[
        'i-045a754bb6ea65723',
    ]
)
