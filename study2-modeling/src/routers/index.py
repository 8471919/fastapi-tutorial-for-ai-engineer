from fastapi import APIRouter
from src.routers.user import user_router
from src.routers.post import post_router
from src.routers.house import house_router

index_router = router = APIRouter()

router.include_router(user_router, prefix="/user")
router.include_router(post_router, prefix="/post")
router.include_router(house_router, prefix="/house")