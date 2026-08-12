"""
todo_tool.py

A simple local to-do list, stored as JSON on disk.
Good enough to start — can swap for a real database or
a service like Todoist later.
"""

import json
import os

TODO_FILE = "todo_list.json"


def _load() -> list:
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)


def _save(items: list) -> None:
    with open(TODO_FILE, "w") as f:
        json.dump(items, f, indent=2)


def add_todo(task: str) -> str:
    """Add a task to the to-do list."""
    items = _load()
    items.append({"task": task, "done": False})
    _save(items)
    return f"Added '{task}' to your to-do list."


def complete_todo(task_query: str) -> str:
    """Mark a task as done, matched by partial text."""
    items = _load()
    for item in items:
        if task_query.lower() in item["task"].lower():
            item["done"] = True
            _save(items)
            return f"Marked '{item['task']}' as done."
    return f"Couldn't find a task matching '{task_query}'."


def list_todos() -> str:
    """Return a readable summary of pending tasks."""
    items = _load()
    pending = [i["task"] for i in items if not i["done"]]
    if not pending:
        return "Your to-do list is empty."
    return "Pending tasks: " + "; ".join(pending)


# Tool definitions Claude will see
TODO_TOOL_SCHEMAS = [
    {
        "name": "add_todo",
        "description": "Add a task to the user's to-do list.",
        "input_schema": {
            "type": "object",
            "properties": {"task": {"type": "string"}},
            "required": ["task"],
        },
    },
    {
        "name": "complete_todo",
        "description": "Mark a to-do list task as completed.",
        "input_schema": {
            "type": "object",
            "properties": {"task_query": {"type": "string"}},
            "required": ["task_query"],
        },
    },
    {
        "name": "list_todos",
        "description": "List the user's pending to-do items.",
        "input_schema": {"type": "object", "properties": {}},
    },
]
