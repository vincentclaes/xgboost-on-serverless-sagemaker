import json
import boto3
import os

runtime_client = boto3.client("runtime.sagemaker")
sagemaker_endpoint_name = os.environ["SAGEMAKER_ENDPOINT_NAME"]

def handler(event, context):

    print(f"making a prediction on the text: {event['body']}")
    
    response = runtime_client.invoke_endpoint(
        Body=event["body"],
        EndpointName=sagemaker_endpoint_name,
        Accept="application/json",
        ContentType="application/json",
    )
    
    print(f"prediction: {response}")

    return {
        'statusCode': 200,
        'body': json.dumps(prediction)
    }
