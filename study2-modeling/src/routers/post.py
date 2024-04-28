from typing import Optional
from fastapi import APIRouter

post_router = router = APIRouter()

@router.get("/")
async def getHelloPost():
  return "Hello, Post!"

@router.get("/{number}")
async def getPost(number: int, content: Optional[str]=None, isArticle: bool = False):
  return { "message" : f"{number} 번째 포스트입니다.", "content": content, "isArticle": isArticle }