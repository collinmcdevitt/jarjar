"""
brain.py

The decision-making core. Takes a transcribed voice command,
sends it to Claude with a list of available tools, and either:
  - gets back a tool call to execute (send_email, add_event, etc.)
  - gets back a plain text answer (for research/questions)

This is where "tool use" / function calling happens.
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

from email_tool import send_email, EMAIL_TOOL_SCHEMA
from calendar_tool import add_event, remove_event, CALENDAR_TOOL_SCHEMAS
from todo_tool import add_todo, complete_todo, list_todos, TODO_TOOL_SCHEMAS

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Map tool names to the actual Python functions that run them
TOOL_FUNCTIONS = {
    "send_email": send_email,
    "add_event": add_event,
    "remove_event": remove_event,
    "add_todo": add_todo,
    "complete_todo": complete_todo,
    "list_todos": list_todos,
}

ALL_TOOLS = (
    [EMAIL_TOOL_SCHEMA]
    + CALENDAR_TOOL_SCHEMAS
    + TODO_TOOL_SCHEMAS
    # Claude's built-in web search — uncomment once you're ready for research:
    # + [{"type": "web_search_20250305", "name": "web_search"}]
)

SYSTEM_PROMPT = """You are Jarvis, a helpful voice assistant running on the user's
Mac. You have tools to send emails, manage their Google Calendar, and manage a
to-do list. Use tools when the user's request clearly maps to one. Keep spoken
responses short and natural, since they'll be read aloud via text-to-speech."""


def handle_command(transcript: str) -> str:
    """
    Send a transcribed voice command to Claude, execute any tool
    calls it makes, and return a final natural-language response
    to be spoken back to the user.
    """
    messages = [{"role": "user", "content": transcript}]

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        tools=ALL_TOOLS,
        messages=messages,
    )

    # TODO: this needs a loop to handle multi-step tool use properly.
    # Rough shape:
    # while response.stop_reason == "tool_use":
    #     - find the tool_use block(s) in response.content
    #     - call TOOL_FUNCTIONS[block.name](**block.input)
    #     - append the tool result to messages
    #     - call client.messages.create(...) again
    #     - repeat until stop_reason != "tool_use"
    # Then return the final text block.

    raise NotImplementedError("Tool-use loop not implemented yet — see TODO above")
