from fastapi import FastAPI
from src.routers.index import index_router

app = FastAPI()

app.include_router(index_router, prefix="/api")

# / 라는 url로 GET 요청이 들어오면 root함수를 실행시키겠다.  
@app.get("/")
async def root():
  return {"message": "Hello World"}