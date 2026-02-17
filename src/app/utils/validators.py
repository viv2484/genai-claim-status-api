def validate_claim_id(claim_id: str) -> bool:
    return claim_id.startswith("CLM") and len(claim_id) >= 6
