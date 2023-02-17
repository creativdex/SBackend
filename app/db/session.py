from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker ,AsyncSession
from app.config import settings


async_engine = create_async_engine(settings.POSTGRES_DATABASE_URI, future=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
