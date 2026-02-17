from pydantic import BaseModel

class SummaryResponse(BaseModel):
    overallSummary: str
    customerSummary: str
    adjusterSummary: str
    recommendedNextStep: str
