from typing import Generator

import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()