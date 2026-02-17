import boto3
import os

s3 = boto3.client("s3", region_name="us-east-1")
BUCKET_NAME = os.getenv("NOTES_BUCKET", "claims-notes-bucket")

def get_claim_notes(key: str):
    response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
    return response["Body"].read().decode("utf-8")
