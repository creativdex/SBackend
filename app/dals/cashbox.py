from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cashbox import CashboxDB
from app.schemas.cashbox import CashboxIn


class CashboxDAL:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_cashbox(self, cashbox: CashboxIn) -> CashboxDB:
        """Создание кассы в БД"""
        cashbox_db = CashboxDB(name=cashbox.name, division_id=cashbox.division_id)
        self.session.add(cashbox_db)
        await self.session.commit()
        await self.session.refresh(cashbox_db)
        return cashbox_db

    async def get_all(self) -> list[CashboxDB]:
        """Получение списка касс"""
        query = select(CashboxDB)
        result = await self.session.execute(query)
        rows = result.fetchall()
        cashboxs: list[CashboxDB] = [row[0] for row in rows]
        return cashboxs

    async def get_by_id(self, id: int) -> CashboxDB:
        """Получение кассы по ID"""
        query = select(CashboxDB).where(CashboxDB.id == id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def delete_by_id(self, id: int) -> None:
        """Удаление кассы"""
        query = delete(CashboxDB).where(CashboxDB.id == id)
        await self.session.execute(query)
        await self.session.commit()
