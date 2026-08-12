"""
email_tool.py

Handles sending emails through the Gmail API.

Setup needed (on the Mac):
1. Go to console.cloud.google.com, create a project
2. Enable the "Gmail API"
3. Create OAuth 2.0 credentials (Desktop app type)
4. Download the file, rename it credentials.json, put it in this folder
5. First run will open a browser to authorize — this creates token.json automatically

TODO: implement using google-api-python-client
"""


def send_email(to: str, subject: str, body: str) -> str:
    """
    Send an email via Gmail.

    Args:
        to: recipient email address
        subject: email subject line
        body: email body text

    Returns:
        A string confirming success or describing the error,
        so Claude can report back to the user in natural language.
    """
    # TODO:
    # 1. Authenticate using credentials.json / token.json
    # 2. Build the Gmail API service object
    # 3. Construct the MIME message
    # 4. Call service.users().messages().send(...)
    # 5. Return a friendly confirmation string
    raise NotImplementedError("send_email not implemented yet")


# Tool definition Claude will see (used in brain.py when calling the API)
EMAIL_TOOL_SCHEMA = {
    "name": "send_email",
    "description": "Send an email on the user's behalf via Gmail.",
    "input_schema": {
        "type": "object",
        "properties": {
            "to": {"type": "string", "description": "Recipient email address"},
            "subject": {"type": "string", "description": "Subject line"},
            "body": {"type": "string", "description": "Body of the email"},
        },
        "required": ["to", "subject", "body"],
    },
}
