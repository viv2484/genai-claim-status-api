import boto3
import json
import os

bedrock = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"))

MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-sonnet-20240229-v1:0")

def build_prompt(notes: str):
    return f"""
You are an insurance claims assistant.

Given the claim notes below, generate:
1. overallSummary
2. customerSummary
3. adjusterSummary
4. recommendedNextStep

Return strictly in JSON format.

<NOTES>
{notes}
</NOTES>
"""

def summarize_notes(notes: str):
    prompt = build_prompt(notes)

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())
    content = result["content"][0]["text"]

    try:
        return json.loads(content)
    except:
        return {"raw_output": content}
