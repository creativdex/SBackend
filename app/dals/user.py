from uuid import UUID
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserDB
from app.schemas.user import UserIn


class UserDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user: UserIn) -> UserDB:
        """Создание пользователя в БД"""
        user_db = UserDB(
            tg_id=user.tg_id or None,
            name=user.name,
            phone=user.phone,
            city_id=user.city_id,
        )
        self.session.add(user_db)
        await self.session.commit()
        await self.session.refresh(user_db)
        return user_db

    async def update_user(self, user: UserIn) -> UserDB:  # TODO Add Update user
        pass

    async def get_all(self) -> list[UserDB]:
        """Получение списка пользователей"""
        query = select(UserDB)
        result = await self.session.execute(query)
        rows = result.fetchall()
        users: list[UserDB] = [row[0] for row in rows]
        return users

    async def get_by_phone(self, phone: str) -> UserDB:
        """Получение пользователя по телефону"""
        query = select(UserDB).where(UserDB.phone == phone)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_by_tg_id(self, tg_id: str) -> UserDB:
        """Получение пользователя по телефону"""
        query = select(UserDB).where(UserDB.tg_id == tg_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_by_uuid(self, uuid: str) -> UserDB:
        """Получение пользователя"""
        if await self.check_uuid(uuid):
            query = select(UserDB).where(UserDB.user_id == uuid)
            result = await self.session.execute(query)
            return result.scalars().first()
        else:
            return None

    async def get_by_something(self, something) -> UserDB:
        user = await self.get_by_uuid(something)
        if user is None:
            user = await self.get_by_tg_id(something)
        if user is None:
            user = await self.get_by_phone(something)
        if user is None:
            return None
        return user

    async def delete_by_phone(self, phone: str) -> None:
        """Удаление пользователя"""
        query = delete(UserDB).where(UserDB.phone == phone)
        await self.session.execute(query)
        await self.session.commit()

    @staticmethod
    async def check_uuid(uuid: str):
        try:
            UUID(str(uuid))
            return True
        except ValueError:
            return False
