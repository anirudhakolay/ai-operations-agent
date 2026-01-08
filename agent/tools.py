def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid calculation"

def search_tool(query):
    return f"Search result for: {query}"
