"""
calendar_tool.py

Adds and removes events on the user's Google Calendar.

Setup needed (on the Mac):
1. Same Google Cloud project as email_tool.py
2. Enable the "Google Calendar API"
3. Reuse the same credentials.json (Gmail + Calendar scopes can share one OAuth app)

TODO: implement using google-api-python-client
"""


def add_event(title: str, start_time: str, end_time: str, description: str = "") -> str:
    """
    Add an event to the user's primary Google Calendar.

    Args:
        title: event title
        start_time: ISO 8601 datetime string, e.g. "2026-08-12T15:00:00"
        end_time: ISO 8601 datetime string
        description: optional event details

    Returns:
        Confirmation string for Claude to relay to the user.
    """
    # TODO:
    # 1. Authenticate (reuse token.json from email_tool if scopes match)
    # 2. Build the Calendar API service
    # 3. Call service.events().insert(calendarId='primary', body={...})
    raise NotImplementedError("add_event not implemented yet")


def remove_event(event_query: str) -> str:
    """
    Find and remove an event matching a description (e.g. "dentist appointment").

    Args:
        event_query: text to search for in event titles

    Returns:
        Confirmation string for Claude to relay to the user.
    """
    # TODO:
    # 1. Search upcoming events with service.events().list(...)
    # 2. Find best match to event_query
    # 3. Call service.events().delete(...)
    # 4. Handle "no match found" and "multiple matches" cases gracefully
    raise NotImplementedError("remove_event not implemented yet")


# Tool definitions Claude will see
CALENDAR_TOOL_SCHEMAS = [
    {
        "name": "add_event",
        "description": "Add an event to the user's Google Calendar.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start_time": {"type": "string", "description": "ISO 8601 datetime"},
                "end_time": {"type": "string", "description": "ISO 8601 datetime"},
                "description": {"type": "string"},
            },
            "required": ["title", "start_time", "end_time"],
        },
    },
    {
        "name": "remove_event",
        "description": "Remove an event from the user's Google Calendar by matching its title.",
        "input_schema": {
            "type": "object",
            "properties": {
                "event_query": {"type": "string", "description": "Text to match against event titles"},
            },
            "required": ["event_query"],
        },
    },
]
