import boto3

session = boto3.session.Session(aws_access_key_id='XXXXXXXXXXXXXXXXXXXX', aws_secret_access_key='YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
client = session.client('iam')
resp = client.list_users()
print("Able to access iam user list:")
print(resp)
