import boto3

session = boto3.session.Session(aws_access_key_id='AKIASU566IV2ZQPCWQfd', aws_secret_access_key='ZO+zFDVZxe8qJ9W9wWxwaYaNc9lxB1zOxTz/9gfr')
client = session.client('iam')
resp = client.list_users()
print("Able to access iam user list:")
print(resp)
