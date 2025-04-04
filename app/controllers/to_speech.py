from fastapi import APIRouter, Depends, HTTPException
from ..models.schemas import TextToSpeechRequest
from ..services.tts_service import TextToSpeechService

router = APIRouter()


@router.post("/to_speech")
async def to_speech(
    request: TextToSpeechRequest,
    tts_service: TextToSpeechService = Depends(TextToSpeechService),
):
    try:
        file_path = tts_service.generate_speech(
            request.text, request.output_file)
        return {"file": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
