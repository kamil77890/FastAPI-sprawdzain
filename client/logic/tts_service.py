import requests


class TextToSpeechService:
    BASE_URL = 'http://127.0.0.1:5000'

    @staticmethod
    def send_text_to_speech(text: str, output_file=None) -> None:
        response = requests.post(
            f'{TextToSpeechService.BASE_URL}/to_speech', json={'text': text, 'output_file': output_file})
        if response.status_code == 200:
            file_path = response.json().get('file')
            if output_file:
                print(f"Plik audio zapisano jako '{file_path}'.")
        else:
            print(
                f"Błąd: {response.status_code}, {response.json().get('detail')}")

    @staticmethod
    def set_parameter(parameter: str, value) -> None:
        response = requests.patch(
            f'{TextToSpeechService.BASE_URL}/set_parameters', json={'parameter': parameter, 'value': value})
        if response.status_code == 200:
            print(f"Parametr '{parameter}' ustawiono na '{value}'.")
        else:
            print(
                f"Błąd: {response.status_code}, {response.json().get('detail')}")
