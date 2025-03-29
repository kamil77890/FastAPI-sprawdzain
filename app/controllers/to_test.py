from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/")
async def test():
    try:
        return {"message": "Test endpoint is working"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
