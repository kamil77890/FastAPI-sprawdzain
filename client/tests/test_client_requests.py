import os
import uuid
from ...client.logic.tts_service import TextToSpeechService


def test_set_parameter_success():
    TextToSpeechService.set_parameter("rate", 120)
    assert True


def test_send_text_to_speech_direct_text():
    filename = f"test.mp3"
    TextToSpeechService.send_text_to_speech("To jest test.", filename)

    assert os.path.exists(filename)
    os.remove(filename)
