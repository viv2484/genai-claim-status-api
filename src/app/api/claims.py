from fastapi import APIRouter, HTTPException
from app.services.dynamodb_service import get_claim

router = APIRouter()

@router.get("/claims/{claim_id}")
def get_claim_status(claim_id: str):
    claim = get_claim(claim_id)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    return claim
