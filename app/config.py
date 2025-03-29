from pathlib import Path

AUDIO_DIR = Path("audio_files")
AUDIO_DIR.mkdir(exist_ok=True)

SYNTHESIZER_PARAMS = {
    "rate": 200,
    "volume": 1.0,
    "voice": None
}
