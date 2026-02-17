from fastapi import APIRouter, HTTPException
from app.services.dynamodb_service import get_claim
from app.services.s3_service import get_claim_notes
from app.services.bedrock_service import summarize_notes

router = APIRouter()

@router.post("/claims/{claim_id}/summarize")
def summarize_claim(claim_id: str):
    claim = get_claim(claim_id)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")

    notes = get_claim_notes(claim["notesS3Key"])
    if not notes:
        raise HTTPException(status_code=404, detail="Notes not found")

    summary = summarize_notes(notes)
    return summary
