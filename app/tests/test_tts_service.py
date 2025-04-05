import pytest
from app.services.tts_service import TextToSpeechService


def test_generate_speech():
    service = TextToSpeechService()
    text = "To jest test"
    file_path = service.generate_speech(text)

    assert file_path.endswith(".mp3")


def test_set_synthesizer_param_valid():
    service = TextToSpeechService()
    assert service.set_synthesizer_param(
        "rate", 150) is None


def test_set_synthesizer_param_invalid():
    service = TextToSpeechService()
    with pytest.raises(ValueError):
        service.set_synthesizer_param("nonexistent_param", 123)
