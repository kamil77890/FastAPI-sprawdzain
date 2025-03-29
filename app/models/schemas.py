from pydantic import BaseModel


class TextToSpeechRequest(BaseModel):
    text: str
    output_file: str | None = None


class SetParameterRequest(BaseModel):
    parameter: str
    value: int | float | str
