from config.argument_parser import set_arguments
from logic.tts_service import TextToSpeechService
from logic.file_manager import FileManager


class Client:
    def __init__(self):
        self.parser = set_arguments()
        self.args = self.parser.parse_args()

    def start(self):
        if self.args.parameter:
            param_name, param_value = self.args.parameter
            TextToSpeechService.set_parameter(param_name, param_value)
        elif self.args.source and self.args.output:
            text = FileManager.read_text_file(self.args.source)
            if text:
                TextToSpeechService.send_text_to_speech(text, self.args.output)
        elif self.args.text:
            TextToSpeechService.send_text_to_speech(
                self.args.text, self.args.output)
        else:
            self.parser.print_help()


if __name__ == "__main__":
    client = Client()
    client.start()
