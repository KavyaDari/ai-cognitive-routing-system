from langchain.tools import tool
from app.config import llm
from app.utils import extract_json

@tool
def mock_searxng_search(query: str):
    """Mock search tool that returns fake news headlines."""
    
    if "crypto" in query.lower():
        return "Bitcoin hits all-time high after ETF approval"
    if "ai" in query.lower():
        return "New AI model threatens developer jobs"
    return "Tech industry trends upward"


# NODE 1
def decide_search(state):
    persona = state.get("persona", "")
    bot_id = state.get("bot_id")

    topic = llm.invoke(f"""
    You are:
    {persona}

    Decide ONE topic to post about today.
    Output only short topic.
    """).content.strip()

    return {
        "persona": persona,
        "topic": topic,
        "bot_id": bot_id
    }


# NODE 2
def search(state):
    topic = state.get("topic", "AI news")

    results = mock_searxng_search.invoke({"query": topic})

    return {
        "persona": state.get("persona"),
        "topic": topic,
        "context": results,
        "bot_id": state.get("bot_id")
    }


# NODE 3
def draft(state):
    persona = state.get("persona", "")
    context = state.get("context", "")
    topic = state.get("topic", "")
    bot_id = state.get("bot_id")

    response = llm.invoke(f"""
    Persona:
    {persona}

    Context:
    {context}

    Write a strong opinionated tweet under 280 characters.

    OUTPUT STRICT JSON:
    {{
        "bot_id": "{bot_id}",
        "topic": "{topic}",
        "post_content": "..."
    }}
    """).content

    final_output = extract_json(response)

    return {
        "persona": persona,
        "topic": topic,
        "context": context,
        "bot_id": bot_id,
        "final": final_output
    }