"""
transcribe.py

Converts recorded audio into text using OpenAI's Whisper model,
run locally (no API key needed, no cost, works offline).

Setup needed (on the Mac):
1. pip install openai-whisper
2. Also needs ffmpeg: `brew install ffmpeg`

TODO: implement
"""

import whisper

_model = None


def _get_model():
    global _model
    if _model is None:
        # "base" is a good speed/accuracy tradeoff to start.
        # Options: tiny, base, small, medium, large
        _model = whisper.load_model("base")
    return _model


def transcribe_audio(file_path: str) -> str:
    """
    Transcribe a recorded audio file to text.

    Args:
        file_path: path to a .wav (or other supported) audio file

    Returns:
        The transcribed text.
    """
    model = _get_model()
    result = model.transcribe(file_path)
    return result["text"].strip()
