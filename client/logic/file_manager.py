class FileManager:
    @staticmethod
    def read_text_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Plik '{file_path}' nie został znaleziony.")
            return None

    @staticmethod
    def save_audio_file(content, file_path):
        try:
            with open(file_path, 'wb') as f:
                f.write(content)
            print(f"Plik audio zapisano jako '{file_path}'.")
        except IOError as e:
            print(f"Błąd podczas zapisywania pliku '{file_path}': {e}")
