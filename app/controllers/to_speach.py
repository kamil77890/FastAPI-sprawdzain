from fastapi import APIRouter, HTTPException
from ..models.schemas import TextToSpeechRequest
from ..services.tts_service import TextToSpeechService

router = APIRouter()


@router.post("/to_speech")
async def to_speech(request: TextToSpeechRequest):
    try:
        file_path = TextToSpeechService.generate_speech(
            request.text, request.output_file)
        return {"file": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
