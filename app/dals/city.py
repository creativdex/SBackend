from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.city import CityDB
from app.schemas.city import CityIn


class CityDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_city(self, city: CityIn) -> CityDB:
        """Создание города в БД"""
        city_db = CityDB(name=city.name)
        self.session.add(city_db)
        await self.session.commit()
        await self.session.refresh(city_db)
        return city_db

    async def get_all(self) -> list[CityDB]:
        """Получение списка городов"""
        query = select(CityDB)
        result = await self.session.execute(query)
        rows = result.fetchall()
        cities: list[CityDB] = [row[0] for row in rows]
        return cities

    async def get_by_id(self, id: int) -> CityDB:
        """Получение города по ID"""
        query = select(CityDB).where(CityDB.id == id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def delete_by_id(self, id: int) -> None:
        """Удаление города"""
        query = delete(CityDB).where(CityDB.id == id)
        await self.session.execute(query)
        await self.session.commit()
