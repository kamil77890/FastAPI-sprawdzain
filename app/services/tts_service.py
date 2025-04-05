from ..data_access.data_access import DataAccess

data_access = DataAccess()


class TextToSpeechService:
    @staticmethod
    def generate_speech(text: str, output_file: str = None):
        return data_access.save_audio(text, output_file)

    @staticmethod
    def set_synthesizer_param(param: str, value):
        if not data_access.update_param(param, value):
            raise ValueError("Zła wartość parametru")
