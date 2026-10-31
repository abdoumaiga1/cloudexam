
import boto3
import os

DYNAMODB_ENDPOINT = os.getenv(
    "DYNAMODB_ENDPOINT",
    "http://localhost:8000"
)

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url=DYNAMODB_ENDPOINT,
    region_name="us-east-1",
    aws_access_key_id="local",
    aws_secret_access_key="local"
)

table = dynamodb.Table("CloudExamSubmissions")


def save_submission(submission):
    """
    Save an examination submission to DynamoDB Local.
    """

    table.put_item(Item=submission)

    return {
        "message": "Submission saved successfully",
        "submission_id": submission["submission_id"]
    }
