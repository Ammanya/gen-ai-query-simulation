from fastapi import APIRouter
from app.utils.query_translator import explain_query

router = APIRouter()

@router.get("/", summary="Explain Query")
async def explain_query_endpoint(query: str):
    explanation = explain_query(query)
    return {"explanation": explanation}
