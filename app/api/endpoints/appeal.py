from fastapi import APIRouter, Depends, HTTPException  # noqa
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.config import logger
from app.dals.appeal import AppealDAL
from app.schemas.appeal import Appeal, AppealIn
from app.db.session import get_session

router = APIRouter()


@router.post("/add_appeal", response_model=Appeal)
async def add_appeal(body: AppealIn, session: AsyncSession = Depends(get_session)):
    appeal_dal = AppealDAL(session)
    try:
        new_appeal = await appeal_dal.create_appeal(body)
        return new_appeal
    except IntegrityError as e:
        text = e.args[0].split(">:")
        logger.error(e, exc_info=False)
        raise HTTPException(status_code=422, detail=text)
