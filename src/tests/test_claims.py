from app.utils.validators import validate_claim_id

def test_validate_claim_id():
    assert validate_claim_id("CLM1001") is True
    assert validate_claim_id("1001") is False
