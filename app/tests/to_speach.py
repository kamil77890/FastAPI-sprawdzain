from fastapi.testclient import TestClient
from ..main import Application
from ..models.schemas import TextToSpeechRequest

client = TestClient(Application().app)


def test_to_speech():
    request_data = TextToSpeechRequest(
        text="Przykładowy tekst", output_file="output.mp3")

    response = client.post("/to_speech", json=request_data.dict())
    assert response.status_code == 200
