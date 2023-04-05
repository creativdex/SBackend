from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.division import DivisionDB
from app.schemas.division import DivisionIn


class DivisionDAL:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_division(self, division: DivisionIn) -> DivisionDB:
        """Создание подразделения в БД"""
        division_db = DivisionDB(name=division.name, city_id=division.city_id)
        self.session.add(division_db)
        await self.session.commit()
        await self.session.refresh(division_db)
        return division_db

    async def get_all(self) -> list[DivisionDB]:
        """Получение списка подразделений"""
        query = select(DivisionDB)
        result = await self.session.execute(query)
        rows = result.fetchall()
        division: list[DivisionDB] = [row[0] for row in rows]
        return division

    async def get_by_id(self, id: int) -> DivisionDB:
        """Получение подразделения по ID"""
        query = select(DivisionDB).where(DivisionDB.id == id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_by_city_id(self, id: int) -> DivisionDB:
        """Получение подразделения по ID"""
        query = select(DivisionDB).where(DivisionDB.city_id == id)
        result = await self.session.execute(query)
        rows = result.fetchall()
        division: list[DivisionDB] = [row[0] for row in rows]
        return division

    async def delete_by_id(self, id: int) -> None:
        """Удаление подразделения"""
        query = delete(DivisionDB).where(DivisionDB.id == id)
        await self.session.execute(query)
        await self.session.commit()
