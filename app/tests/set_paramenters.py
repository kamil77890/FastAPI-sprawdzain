from fastapi.testclient import TestClient
from app.main import Application
from app.models.schemas import SetParameterRequest

client = TestClient(Application().app)


def test_set_parameters():
    request_data = SetParameterRequest(parameter="rate", value="150")

    response = client.patch("/set_parameters", json=request_data.dict())
    assert response.json() == {"message": "Parameters set successfully"}
