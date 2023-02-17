from fastapi import APIRouter
from app.api.endpoints import users, city

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(city.router, prefix="/city", tags=["city"])
