from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.division import DivisionDB
from app.schemas.division import DivisionIn

class DivisionDAL:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
    
    async def create_division(self, division: DivisionIn) -> DivisionDB:
        """Создание подразделения в БД"""    
        division_db = DivisionDB(
            name = division.name,
            city_id = division.city_id
        )
        self.session.add(division_db)
        await self.session.commit()
        await self.session.refresh(division_db)
        return division_db
