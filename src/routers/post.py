from fastapi import APIRouter

post_router = router = APIRouter()

@router.get("/{number}")
async def getPost(number: str):
  return { "message" : f"{number} 번째 포스트입니다."}