import boto3, uuid

client = boto3.client('iotsitewise')

response = client.create_asset(
    assetName='Roboterzelle',
    assetModelId=str(uuid.uuid1())+"Roboterzelle",
)