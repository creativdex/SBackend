from fastapi import APIRouter
from app.api.endpoints import users, city, division, cashbox, type_of_problem

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(city.router, prefix="/city", tags=["city"])
router.include_router(division.router, prefix="/division", tags=["division"])
router.include_router(cashbox.router, prefix="/cashbox", tags=["cashbox"])
router.include_router(
    type_of_problem.router, prefix="/type_of_problem", tags=["type_of_problem"]
)
