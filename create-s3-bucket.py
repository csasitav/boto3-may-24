import boto3
client = boto3.client("s3")
response = client.create_bucket(
    ACL='private',
    Bucket='jhc-24-boto-demo',
)
print(response)