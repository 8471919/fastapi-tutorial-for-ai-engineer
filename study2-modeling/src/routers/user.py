from fastapi import APIRouter
from pydantic import BaseModel

user_router = router = APIRouter()

class CreatePostBodyDto(BaseModel):
  name: str
  age: int
  height: int

class CreateUserByUsernameBodyDto(BaseModel):
  height: int
  weight: int

@router.get("/")
async def getUser(nickname: str, age: int):
  return {"nickname": nickname, "age": age}

@router.post("/{username}")
async def createUserByUsername(body: CreateUserByUsernameBodyDto, username: str, age: int):
  height = body.height
  weight = body.weight
  
  processed_height = f"{height}cm"
  processed_weight = f"{weight}kg"
  
  return {"username": username, "age": age, "height": processed_height, "weight": processed_weight}

@router.post("/")
async def createUser(body: CreatePostBodyDto):
  
  name = body.name
  age = body.age
  height = body.height
  
  processed_age = f"{age}살"
  processed_height = f"{height}cm"
  
  return {"name": name, "age": processed_age, "height": processed_height}

