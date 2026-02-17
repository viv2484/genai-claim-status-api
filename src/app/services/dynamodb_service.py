import boto3
import os

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
TABLE_NAME = os.getenv("CLAIMS_TABLE", "claims-table")
table = dynamodb.Table(TABLE_NAME)

def get_claim(claim_id: str):
    response = table.get_item(Key={"claimId": claim_id})
    return response.get("Item")
