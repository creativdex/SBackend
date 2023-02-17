from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dals.city import CityDAL
from app.schemas.city import City, CityIn
from app.db.session import get_session

router = APIRouter()


@router.post("/add_city", response_model=City)
async def add_city(body: CityIn,
                   session: AsyncSession = Depends(get_session)):
    city_dal = CityDAL(session)
    new_city = await city_dal.create_city(body)
    return new_city


@router.get("/get_all", response_model=list[City])
async def get_all_city(session: AsyncSession = Depends(get_session)):
    city_dal = CityDAL(session)
    cities = await city_dal.get_all()
    if cities is None:
        raise HTTPException(status_code=422,
                            detail={'loc': ['body'],
                                    'msg': 'City not found',
                                    'type': 'value_error'})
    else:
        return cities


@router.get("/get/{id}", response_model=City)
async def get_by_id(id: int, session: AsyncSession = Depends(get_session)):
    city_dal = CityDAL(session)
    city = await city_dal.get_by_id(id)
    if city is None:
        raise HTTPException(status_code=422,
                            detail={'loc': ['body','id'],
                                    'msg': 'City not found',
                                    'type': 'value_error'})
    else:
        return city


@router.delete("/delete{id}", status_code=204)
async def delete_by_id(id: int, session: AsyncSession = Depends(get_session)):
    city_dal = CityDAL(session)
    if not await city_dal.get_by_id(id):
        raise HTTPException(status_code=422,
                            detail={'loc': ['body','phone'],
                                    'msg': 'City not found',
                                    'type': 'value_error'})
    await city_dal.delete_by_id(id)
