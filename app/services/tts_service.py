from ..data_access.data_access import DataAccess


class TextToSpeechService:
    @staticmethod
    def generate_speech(text: str, output_file: str = None):
        return DataAccess.save_audio(text, output_file)

    @staticmethod
    def set_synthesizer_param(param: str, value):
        if not DataAccess.update_param(param, value):
            raise ValueError("Zła wartość parametru")
