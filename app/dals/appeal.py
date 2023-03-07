# from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.appeal import AppealDB
from app.schemas.appeal import AppealIn


class AppealDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_appeal(self, appeal: AppealIn) -> AppealDB:
        """Создание пользователя в БД"""
        appeal_db = AppealDB(
            type_of_problem_id=appeal.type_of_problem_id,
            user_id=appeal.user_id,
            division_id=appeal.division_id,
            description=appeal.description,
            files=appeal.files,
        )
        self.session.add(appeal_db)
        await self.session.commit()
        await self.session.refresh(appeal_db)
        return appeal_db

    async def check_input(self, appeal: AppealIn):
        pass
