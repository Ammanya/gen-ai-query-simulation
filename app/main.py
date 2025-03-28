from fastapi import FastAPI
from app.routes.query import router as query_router
from app.routes.explain import router as explain_router
from app.routes.validate import router as validate_router
from app.routes.generate import router as generate_router

# Create FastAPI app instance
app = FastAPI(
    title="Gen AI Query Simulation Engine",
    description="A lightweight backend service for simulating AI-powered query processing.",
    version="1.0.0",
)

# Include route modules
app.include_router(explain_router, prefix="/explain", tags=["Explain Query"])
app.include_router(query_router, prefix="/query", tags=["Query Processing"])
app.include_router(validate_router, prefix="/validate", tags=["Validation"])
app.include_router(generate_router, prefix="/generate", tags=["Generation"])

@app.get("/")
def read_root():
    return {"message": "Gen AI Query Simulation Engine is running!"}
