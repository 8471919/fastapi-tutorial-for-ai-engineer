from fastapi import APIRouter

user_router = router = APIRouter()

@router.get("/hansu")
async def getHansu():
  return { "username": "hansu" }