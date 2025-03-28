from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.query_translator import process_query

router = APIRouter()


# Define the request model
class QueryRequest(BaseModel):
    query: str


# Define the response model
class QueryResponse(BaseModel):
    query_result: str


# Process AI query endpoint
@router.post("/", response_model=QueryResponse)
async def process_ai_query(request: QueryRequest):
    query_result = process_query(request.query)
    if not query_result:
        raise HTTPException(status_code=400, detail="Invalid query or processing error")

    return {"query_result": query_result}
