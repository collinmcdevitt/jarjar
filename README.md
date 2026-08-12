# jarjar

A voice-activated personal assistant for Mac, inspired by Iron Man's J.A.R.V.I.S.

## Features (planned)
- [ ] Voice activation (wake word: "Hey Jarvis")
- [ ] Send emails via Gmail
- [ ] Add / remove Google Calendar events
- [ ] Pull together research on a topic
- [ ] Maintain a working to-do list

## Architecture

1. **Wake word detection** — listens locally for "Hey Jarvis"
2. **Speech-to-text** — transcribes the command that follows
3. **The Brain** — Claude API decides what the user wants and picks a tool to call
4. **Tools** — actual Python functions that do the work (send email, edit calendar, etc.)
5. **Text-to-speech** — Jarvis speaks a response back

```
voice --> wake word --> transcribe --> Claude (decides + calls tool) --> tool runs --> speaks result
```

## Tech stack
- **Language:** Python 3.11+
- **Wake word:** Picovoice Porcupine
- **Speech-to-text:** OpenAI Whisper (local)
- **Text-to-speech:** macOS `say` command (swap for ElevenLabs later)
- **Brain:** Anthropic Claude API (tool use / function calling)
- **Email:** Gmail API
- **Calendar:** Google Calendar API
- **To-do list:** local JSON file to start (swap for a real DB/service later)

## Build order

1. Record + transcribe voice with Whisper — confirm the mic pipeline works
2. Send transcript to Claude API, print the response — confirm the brain works
3. Add `send_email` tool, wire up Gmail API, let Claude call it
4. Add calendar add/remove tools, wire up Google Calendar API
5. Add to-do list tool (local file)
6. Add research/web search tool
7. Add wake word listener so it runs hands-free in the background
8. (Optional) Wrap as a macOS menu bar app with `rumps`

## Setup (do this on the Mac, not the phone)

```bash
git clone <your-repo-url>
cd jarvis-assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in your API keys
```

## File structure

```
jarvis-assistant/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── main.py              # entry point, wires everything together
├── brain.py             # talks to Claude API, decides which tool to call
├── email_tool.py         # Gmail send
├── calendar_tool.py     # Google Calendar add/remove
├── todo_tool.py          # local to-do list
├── research_tool.py     # web research / search
└── voice/
    ├── listen.py         # wake word + recording
    ├── transcribe.py     # Whisper speech-to-text
    └── speak.py          # text-to-speech
```

## Status
🚧 Just getting started. Skeleton files are stubbed out with comments — fill in the logic on the Mac where audio/API testing is actually possible.