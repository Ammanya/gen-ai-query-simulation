# Query processing logic
def process_query(query: str) -> str:
    if not query:
        return None

    # Basic example: Simulate processing query and returning a response
    if "weather" in query.lower():
        return "The weather today is sunny with a high of 25°C."
    elif "time" in query.lower():
        return "The current time is 3:00 PM."
    elif "news" in query.lower():
        return "Here are the latest headlines: AI is changing the world!"

    # Default response
    return "I'm not sure how to respond to that query."


# Explain query logic
def explain_query(query: str) -> str:
    if not query:
        return "No query provided."

    # Simple explanations
    if "weather" in query.lower():
        return "This query is asking about the current weather."
    elif "time" in query.lower():
        return "This query is asking for the current time."
    elif "news" in query.lower():
        return "This query is requesting recent news updates."

    return "This query is not recognized or requires further processing."
