import re

def validate_query(query: str) -> bool:
    """
    Validate the natural language query by matching it against
    predefined valid patterns or acceptable query structures.
    """

    # Define a list of valid patterns/phrases to match
    valid_patterns = [
        r"total sales of last month",
        r"total revenue for this week",
        r"number of orders yesterday",
        r"average profit for the last quarter",
        r"sales data for (january|february|march|april|may|june|july|august|september|october|november|december)",
        r"how many products were sold last month",
        r"get me the sales summary for last month",
        r"get.*total sales.*last month",  # Added flexible pattern
        r"show.*revenue.*week",
        r"number.*orders.*yesterday"
    ]

    # Check if any valid pattern matches the query
    for pattern in valid_patterns:
        if re.search(pattern, query, re.IGNORECASE):
            return True

    # Return False if no match is found
    return False
