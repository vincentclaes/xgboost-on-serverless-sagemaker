import json
import boto3
import os

runtime_client = boto3.client("runtime.sagemaker")
sagemaker_endpoint_name = os.environ["SAGEMAKER_ENDPOINT_NAME"]

def handler(event, context):
    
    data = event["body"]["data"]
    content_type = event["body"]["content_type"]
    
    print(f"making a prediction on the data: {data}")
    
    response = runtime_client.invoke_endpoint(
        EndpointName=sagemaker_endpoint_name,
        Body=data,
        ContentType=content_type,

    )
    prediction = response["Body"].read()

    
    print(f"prediction: {prediction}")
    return {
        'statusCode': 200,
        'body': prediction
    }
