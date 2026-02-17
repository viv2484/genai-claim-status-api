from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uuid
import logging

from app.api.claims import router as claims_router
from app.api.summarize import router as summarize_router

app = FastAPI(title="GenAI Claim Status API")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.middleware("http")
async def add_correlation_id(request: Request, call_next):
    correlation_id = str(uuid.uuid4())
    request.state.correlation_id = correlation_id
    response = await call_next(request)
    response.headers["X-Correlation-ID"] = correlation_id
    return response

app.include_router(claims_router)
app.include_router(summarize_router)

@app.get("/health")
def health():
    return {"status": "healthy"}
