📚 Gen AI Query Simulation


📌 Project Overview


Gen AI Query Simulation is a FastAPI-based application that simulates AI responses to queries using OpenAI’s API. The backend is deployed on Render and provides RESTful APIs to handle user queries and generate simulated AI responses.

🚀 Live URL


👉 API Documentation: 
         
         https://gen-ai-query-simulation.onrender.com/docs

🛠️ Tech Stack

         Backend: FastAPI

AI API: OpenAI

Deployment: Render

Documentation: Swagger (Auto-generated at /docs)


📝 Features


✅ Simulates AI-generated responses using OpenAI

✅ RESTful API with request/response models

✅ Error handling for invalid inputs and API failures

✅ Swagger documentation available at /docs


⚡️ Getting Started


🖥️ 1. Clone the Repository

             git clone 

cd gen-ai-query-simulation


📦 2. Create and Activate Virtual Environment

# Create a virtual environment

python3 -m venv venv

# Activate on Mac/Linux

source venv/bin/activate

# Activate on Windows

venv\Scripts\activate


📚 3. Install Dependencies

pip install -r requirements.txt

🔥 4. Set Up Environment Variables

Create a .env file in the root directory and add your OpenAI API key:

OPENAI_API_KEY=your-openai-api-key

▶️ 5. Run the Application

uvicorn main:app --host 0.0.0.0 --port 8000

✅ API will be accessible at:

http://127.0.0.1:8000

Documentation: http://127.0.0.1:8000/docs

📡 API Endpoints
1️⃣ Generate AI Query Response
URL: /generate

Method: POST

Request Body:

json
Copy
Edit
{
  "query": "What is the capital of France?"
}
Response:

json
Copy
Edit
{
  "response": "The capital of France is Paris."
}
2️⃣ Health Check
URL: /health

Method: GET

Response:

json
Copy
Edit
{
  "status": "Healthy"
}
🔎 Testing the API with cURL
1. Generate a Query
bash
Copy
Edit
curl -X POST "https://gen-ai-query-simulation.onrender.com/generate" \
-H "Content-Type: application/json" \
-d '{"query": "What is AI?"}'
2. Health Check
bash
Copy
Edit
curl -X GET "https://gen-ai-query-simulation.onrender.com/health"
📮 Testing with Postman
A Postman Collection is included in the repo.

Import Gen AI Query Simulation.postman_collection.json into Postman.

Test all available endpoints.

🧠 Error Handling
Invalid Query Format → 400 Bad Request

OpenAI API Errors → 500 Internal Server Error

Invalid Endpoint → 404 Not Found

🎁 Postman Collection
Postman collection file is available in the root directory:

graphql
Copy
Edit
/Gen AI Query Simulation.postman_collection.json
📝 Deployment
✅ Deployed on Render:

https://gen-ai-query-simulation.onrender.com/docs

🎯 Future Enhancements
Add user authentication for API access

Implement query caching to optimize responses

Improve error logging and monitoring

