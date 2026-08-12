"""
main.py

Entry point. Ties together: wake word -> record -> transcribe ->
brain (Claude decides + calls tools) -> speak response.

Run with: python main.py

NOTE: Get each piece working on its own first before wiring this
whole loop together. Suggested order (see README.md "Build order"):
  1. voice/transcribe.py — test transcribing a sample .wav file
  2. brain.py — test sending plain text and getting a response
  3. Individual tools (email_tool.py, calendar_tool.py, todo_tool.py)
  4. voice/listen.py — wake word + recording
  5. voice/speak.py — talking back
  6. Then wire it all together here in the loop below.
"""

from voice.listen import listen_for_wake_word, record_command
from voice.transcribe import transcribe_audio
from voice.speak import speak
from brain import handle_command


def main():
    print("Jarvis is running. Waiting for wake word...")
    while True:
        listen_for_wake_word()
        speak("Yes?")

        audio_path = record_command()
        transcript = transcribe_audio(audio_path)
        print(f"Heard: {transcript}")

        response = handle_command(transcript)
        print(f"Jarvis: {response}")
        speak(response)


if __name__ == "__main__":
    main()
