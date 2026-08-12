"""
speak.py

Speaks text out loud. Starts with macOS's built-in `say` command
(free, no setup, decent quality). Can swap for ElevenLabs API later
for a more natural / customizable voice.
"""

import subprocess


def speak(text: str, voice: str = "Samantha") -> None:
    """
    Speak text aloud using macOS's built-in text-to-speech.

    Args:
        text: what to say
        voice: macOS voice name (run `say -v ?` in Terminal to list options)
    """
    subprocess.run(["say", "-v", voice, text])


# TODO (optional upgrade): swap this for ElevenLabs API for a more
# natural / custom "Jarvis" voice. Would need elevenlabs pip package
# and an API key.
