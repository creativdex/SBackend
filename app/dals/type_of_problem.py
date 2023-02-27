from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.type_of_problem import TypeOfProblemDB


class TypeOfProblemDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def update_list(self, list_update: list) -> list[TypeOfProblemDB]:
        """Обновление списка из Битрикса"""
        self.session.add_all(list_update)
        await self.session.commit()
        return list_update

    async def get_all(self) -> list[TypeOfProblemDB]:
        """Получение списка проблем"""
        query = select(TypeOfProblemDB)
        result = await self.session.execute(query)
        rows = result.fetchall()
        types_of_problem: list[TypeOfProblemDB] = [row[0] for row in rows]
        return types_of_problem

    async def get_all_is_show(self) -> list[TypeOfProblemDB]:
        """Получение списка проблем"""
        query = select(TypeOfProblemDB).where(TypeOfProblemDB.is_show)
        result = await self.session.execute(query)
        rows = result.fetchall()
        types_of_problem: list[TypeOfProblemDB] = [row[0] for row in rows]
        return types_of_problem

    async def delete_all(self) -> None:
        """Удаление списка проблем"""
        query = delete(TypeOfProblemDB)
        await self.session.execute(query)
        await self.session.commit()

    async def get_by_id(self, id: int):
        type_of_problem = await self.session.execute(
            select(TypeOfProblemDB).where(TypeOfProblemDB.id == id)
        )
        return type_of_problem.scalars().first()

    async def switch_is_show(self, type_of_problem: TypeOfProblemDB):
        query = (
            update(TypeOfProblemDB)
            .where(TypeOfProblemDB.id == type_of_problem.id)
            .values(is_show=not type_of_problem.is_show)
        )
        await self.session.execute(query)
        await self.session.commit()
        await self.session.refresh(type_of_problem)
        return type_of_problem

    @staticmethod
    async def convert_to_db(list_from_bx: list) -> list:
        """Конвертация списка из битрикса в БД"""
        type_of_problem_db = []
        for item in list_from_bx:
            type_of_problem_db.append(TypeOfProblemDB(id=item["id"], name=item["name"]))
        return type_of_problem_db

    @staticmethod
    async def compare_list(
        list1: list[TypeOfProblemDB], list2: list[TypeOfProblemDB]
    ) -> list[TypeOfProblemDB]:
        list2 = [row.id for row in list2]
        list_difference = [element for element in list1 if element.id not in list2]
        return list_difference
