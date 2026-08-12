"""
listen.py

Listens for the wake word ("Hey Jarvis") using Picovoice Porcupine,
then records the command that follows.

Setup needed (on the Mac):
1. Sign up free at console.picovoice.ai, get an access key
2. `brew install portaudio` (needed for pyaudio)
3. pip install pvporcupine pyaudio

TODO: implement
"""


def listen_for_wake_word() -> None:
    """
    Blocks until the wake word is detected. Runs in a loop,
    listening to the mic in small chunks.
    """
    # TODO:
    # 1. Initialize Porcupine with your access key + wake word model
    # 2. Open a mic audio stream (pyaudio)
    # 3. Feed audio frames to porcupine.process()
    # 4. Return when a wake word is detected
    raise NotImplementedError("listen_for_wake_word not implemented yet")


def record_command(seconds: int = 5) -> str:
    """
    Records audio for a fixed duration (or until silence) after
    the wake word triggers, and saves it to a temp .wav file.

    Returns:
        Path to the recorded audio file.
    """
    # TODO:
    # 1. Open mic stream
    # 2. Record for `seconds` (or use silence detection to auto-stop)
    # 3. Write to a temp .wav file
    # 4. Return the file path
    raise NotImplementedError("record_command not implemented yet")
