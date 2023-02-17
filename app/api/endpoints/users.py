from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dals.user import UserDAL
from app.schemas.user import UserOut, UserIn
from app.db.session import get_session

router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register_new_user(body: UserIn,
                            session: AsyncSession = Depends(get_session)):
    user_dal = UserDAL(session)
    if await user_dal.get_by_phone(body.phone) or await user_dal.get_by_tg_id(body.tg_id) is not None:
        raise HTTPException(status_code=422,
                            detail={'loc': ['body','phone', 'tg_id'],
                                    'msg': 'The phone number or telegram ID is already registered',
                                    'type': 'value_error'})
    else:
        new_user = await user_dal.create_user(body)
        return new_user


@router.get("/get_all", response_model=list[UserOut])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    user_dal = UserDAL(session)
    users = await user_dal.get_all()
    if users is None:
        raise HTTPException(status_code=422,
                            detail={'loc': ['body'],
                                    'msg': 'Users not found',
                                    'type': 'value_error'})
    else:
        return users


@router.get("/get/{phone}", response_model=UserOut)
async def get_by_phone(phone: str, session: AsyncSession = Depends(get_session)):
    user_dal = UserDAL(session)
    user = await user_dal.get_by_phone(phone)
    if user is None:
        raise HTTPException(status_code=422,
                            detail={'loc': ['body','phone'],
                                    'msg': 'User not found',
                                    'type': 'value_error'})
    else:
        return user


@router.get("/get/{tg_id}", response_model=UserOut)
async def get_by_phone(tg_id: int, session: AsyncSession = Depends(get_session)):
    user_dal = UserDAL(session)
    user = await user_dal.get_by_tg_id(tg_id)
    if user is None:
        raise HTTPException(status_code=422,
                            detail={'loc': ['body','tg_id'],
                                    'msg': 'User not found',
                                    'type': 'value_error'})
    else:
        return user


@router.delete("/delete{phone}", status_code=204)
async def delete_by_phone(phone: str, session: AsyncSession = Depends(get_session)):
    user_dal = UserDAL(session)
    if not await user_dal.get_by_phone(phone):
        raise HTTPException(status_code=422,
                            detail={'loc': ['body','phone'],
                                    'msg': 'User not found',
                                    'type': 'value_error'})
    await user_dal.delete_by_phone(phone)
