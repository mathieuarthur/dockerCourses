from fastapi import APIRouter
from services.response import responseService

router = APIRouter(
    prefix="/responses",
    tags=["responses"],
    responses={404: {"description": "Not found"}}
)

@router.get("/", status_code=200)
async def getResponse() -> str:
    return await responseService()