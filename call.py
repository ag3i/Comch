import boto3
import json

def lambda_handler(event, context):
    
    Payload = json.dumps(event) 

    response = boto3.client('lambda').invoke(
        FunctionName='', # Your lamdba function name
        InvocationType='Event',
        Payload=Payload
    )
    
    return {
        "statusCode": 200,
        "text":"招待完了"
    }