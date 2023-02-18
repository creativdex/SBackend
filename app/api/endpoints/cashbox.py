from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dals.cashbox import CashboxDAL
from app.schemas.cashbox import Cashbox, CashboxIn
from app.db.session import get_session

router = APIRouter()


@router.post("/add_cashbox", response_model=Cashbox)
async def add_division(body: CashboxIn,
                       session: AsyncSession = Depends(get_session)):
    cashbox_dal = CashboxDAL(session)
    new_cashbox = await cashbox_dal.create_cashbox(body)
    return new_cashbox


@router.get("/get_all", response_model=list[Cashbox])
async def get_all_cashboxs(session: AsyncSession = Depends(get_session)):
    cashbox_dal = CashboxDAL(session)
    cashbox = await cashbox_dal.get_all()
    if cashbox is None:
        raise HTTPException(status_code=422,
                            detail={'loc': ['body'],
                                    'msg': 'Cashbox not found',
                                    'type': 'value_error'})
    else:
        return cashbox


@router.get("/get/{id}", response_model=Cashbox)
async def get_by_id(id: int, session: AsyncSession = Depends(get_session)):
    cashbox_dal = CashboxDAL(session)
    cashbox = await cashbox_dal.get_by_id(id)
    if cashbox is None:
        raise HTTPException(status_code=422,
                            detail={'loc': ['body','id'],
                                    'msg': 'Cashbox not found',
                                    'type': 'value_error'})
    else:
        return cashbox


@router.delete("/delete{id}", status_code=204)
async def delete_by_id(id: int, session: AsyncSession = Depends(get_session)):
    cashbox_dal = CashboxDAL(session)
    if not await cashbox_dal.get_by_id(id):
        raise HTTPException(status_code=422,
                            detail={'loc': ['body','id'],
                                    'msg': 'Cashbox not found',
                                    'type': 'value_error'})
    await cashbox_dal.delete_by_id(id)