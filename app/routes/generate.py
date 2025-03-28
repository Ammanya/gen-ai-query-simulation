from fastapi import APIRouter
from pydantic import BaseModel
import openai

router = APIRouter()


# Define request body schema
class QueryRequest(BaseModel):
    natural_query: str


# OpenAI API Key
openai.api_key = "your-openai-api-key"


@router.post("/generate/")
def generate_sql(query_request: QueryRequest):
    natural_query = query_request.natural_query

    # Call OpenAI API to convert natural language to SQL
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Or any fine-tuned model
        messages=[
            {"role": "system", "content": "You are an expert at converting natural language to SQL queries."},
            {"role": "user", "content": f"Convert the following natural language to SQL: {natural_query}"}
        ],
        max_tokens=150
    )

    # Extract generated SQL
    sql_query = response['choices'][0]['message']['content'].strip()

    return {"natural_query": natural_query, "sql_query": sql_query}
