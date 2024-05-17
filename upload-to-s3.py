import boto3
client = boto3.client("s3")
with open('javahome.txt', 'rb') as data:
    client.upload_fileobj(data, 'jhc-24-boto-demo', 'javahome.txt')