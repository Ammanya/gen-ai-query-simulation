from fastapi import APIRouter, Query
from pydantic import BaseModel
from app.utils.query_validator import validate_query



# Initialize router
router = APIRouter()

class ValidationResponse(BaseModel):
    query: str
    valid: bool


@router.get("/validate/")
async def validate(natural_query: str = Query(..., alias="natural_query")) -> ValidationResponse:
    """
    Endpoint to validate a natural language query.

    - **natural_query**: The query entered by the user.
    - **Returns**: JSON object with query and validation status.
    """
    # Call query validator
    is_valid = validate_query(natural_query)
    return ValidationResponse(query=natural_query, valid=is_valid)
