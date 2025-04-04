from fastapi import APIRouter, Depends, HTTPException
from ..services.tts_service import TextToSpeechService
from ..models.schemas import SetParameterRequest

router = APIRouter()


@router.patch("/set_parameters")
async def set_parameters(request: SetParameterRequest,
                         tts_service: TextToSpeechService = Depends(TextToSpeechService)):
    try:
        tts_service.set_synthesizer_param(
            request.parameter, request.value)

        return {"message": "Parameters set successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
