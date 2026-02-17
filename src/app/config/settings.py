import os

class Settings:
    claims_table = os.getenv("CLAIMS_TABLE", "claims-table")
    notes_bucket = os.getenv("NOTES_BUCKET", "claims-notes-bucket")
    bedrock_model = os.getenv("BEDROCK_MODEL_ID", "")
    region = os.getenv("AWS_REGION", "us-east-1")

settings = Settings()
