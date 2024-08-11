from typing import AsyncGenerator, Generator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from src.config import DATABASE_URL


print('DATABASE_URL', DATABASE_URL)

Base = declarative_base()

metadata = MetaData()

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# async def get_db() -> Generator:
#     try:
#         session: AsyncSession = async_session()
#         yield session
#     finally:
#         await session.close()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session