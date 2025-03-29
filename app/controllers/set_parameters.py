from fastapi import APIRouter, HTTPException
from ..models.schemas import SetParameterRequest
from ..services.tts_service import TextToSpeechService

router = APIRouter()


@router.patch("/set_parameters")
async def set_parameters(request: SetParameterRequest):
    try:
        TextToSpeechService.set_synthesizer_param(
            request.parameter, request.value)
        return {"message": "Parameters set successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
