"""
research_tool.py

Pulls together research on a topic. Two options:

Option A (simplest): use Claude's built-in web search tool type
in the API call itself — no separate code needed here, just
add {"type": "web_search_20250305", "name": "web_search"} to
the tools list in brain.py.

Option B: wire up a dedicated search API (e.g. Brave Search API,
Tavily) and summarize results yourself. More control, more setup.

Starting with Option A is recommended — fill this file in only
if you outgrow it.
"""


def research_topic(topic: str) -> str:
    """
    Placeholder for a custom research pipeline, if you decide
    you want more control than Claude's built-in web search gives you.

    Args:
        topic: what to research

    Returns:
        A summarized string of findings.
    """
    # TODO (optional, only if not using Claude's built-in web search):
    # 1. Call a search API with `topic`
    # 2. Fetch/summarize top results
    # 3. Return a concise synthesis
    raise NotImplementedError(
        "Not implemented — consider using Claude's built-in web_search tool in brain.py instead"
    )
