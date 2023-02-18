from fastapi import APIRouter
from app.api.endpoints import users, city, division

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(city.router, prefix="/city", tags=["city"])
router.include_router(division.router, prefix="/division", tags=["division"])
