import pyttsx3
import uuid
from ..config import AUDIO_DIR, SYNTHESIZER_PARAMS


class DataAccess:
    @staticmethod
    def save_audio(text: str, filename: str = None) -> str:
        engine = pyttsx3.init()
        engine.setProperty("rate", SYNTHESIZER_PARAMS["rate"])
        engine.setProperty("volume", SYNTHESIZER_PARAMS["volume"])
        if SYNTHESIZER_PARAMS["voice"]:
            engine.setProperty("voice", SYNTHESIZER_PARAMS["voice"])

        filename = filename or f"{uuid.uuid4()}.mp3"
        filepath = AUDIO_DIR / filename
        engine.save_to_file(text, str(filepath))
        engine.runAndWait()
        return str(filepath)

    @staticmethod
    def update_param(param: str, value) -> bool:
        if param in SYNTHESIZER_PARAMS:
            SYNTHESIZER_PARAMS[param] = value
            return True
        return False
