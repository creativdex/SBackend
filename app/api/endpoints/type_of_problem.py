from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.bitrix import Bitrix
from app.dals.type_of_problem import TypeOfProblemDAL
from app.schemas.type_of_problem import TypeOfProblem
from app.db.session import get_session


router = APIRouter()


@router.post("/update_from_bx", response_model=list[TypeOfProblem])
async def update_from_bx(session: AsyncSession = Depends(get_session)):
    type_of_problem_dal = TypeOfProblemDAL(session)
    problem_from_bx = await Bitrix.get_type_of_problem()
    problem_from_bx = await type_of_problem_dal.convert_to_db(problem_from_bx)
    problem_from_db = await type_of_problem_dal.get_all()
    list_of_difirince = await type_of_problem_dal.compare_list(
        problem_from_bx, problem_from_db
    )
    if list_of_difirince == []:
        raise HTTPException(
            status_code=422,
            detail={
                "loc": ["body"],
                "msg": "There is no data to update",
                "type": "value_error",
            },
        )
    list_update = await type_of_problem_dal.update_list(list_of_difirince)
    return list_update


@router.get("/get_all", response_model=list[TypeOfProblem])
async def get_all_type(session: AsyncSession = Depends(get_session)):
    type_of_problem_dal = TypeOfProblemDAL(session)
    type_of_problem = await type_of_problem_dal.get_all()
    if type_of_problem is None:
        raise HTTPException(
            status_code=422,
            detail={
                "loc": ["body"],
                "msg": "Type of problem not found",
                "type": "value_error",
            },
        )
    else:
        return type_of_problem


@router.get("/get_all_is_show", response_model=list[TypeOfProblem])
async def get_all_is_show(session: AsyncSession = Depends(get_session)):
    type_of_problem_dal = TypeOfProblemDAL(session)
    type_of_problem = await type_of_problem_dal.get_all_is_show()
    if type_of_problem == []:
        raise HTTPException(
            status_code=422,
            detail={
                "loc": ["body"],
                "msg": "Type of problem is show not found",
                "type": "value_error",
            },
        )
    else:
        return type_of_problem


@router.get("/switch_is_show/{id}", response_model=TypeOfProblem)
async def switch_is_show(id: int, session: AsyncSession = Depends(get_session)):
    type_of_problem_dal = TypeOfProblemDAL(session)
    type_of_problem = await type_of_problem_dal.get_by_id(id)
    if type_of_problem is None:
        raise HTTPException(
            status_code=422,
            detail={
                "loc": ["body"],
                "msg": "Type of problem not found",
                "type": "value_error",
            },
        )
    return await type_of_problem_dal.switch_is_show(type_of_problem)


@router.delete("/delete_all", status_code=204)
async def delete_all(session: AsyncSession = Depends(get_session)):
    type_of_problem_dal = TypeOfProblemDAL(session)
    if type_of_problem_dal.get_all() is None:
        raise HTTPException(
            status_code=422,
            detail={
                "loc": ["body"],
                "msg": "Type of problem not found",
                "type": "value_error",
            },
        )
    await type_of_problem_dal.delete_all()
