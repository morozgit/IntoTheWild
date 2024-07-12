import asyncio
import platform
from typing import Any, Generator

import pytest
from alembic import command
from alembic.config import Config
from envparse import Env
from sqlalchemy import MetaData, Table
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from backend.db.session import get_db
from backend.src.main import app

CLEAN_TABLES = [
    "locations",
    "tracks",
]

env = Env()

if platform.system() == "Linux":
    TEST_DATABASE_URL = env.str(
        "TEST_DATABASE_URL",
        default="postgresql+asyncpg://postgres:postgres@127.0.0.1:6432/postgres",
    )
elif platform.system() == "Windows":
    TEST_DATABASE_URL = env.str(
        "TEST_DATABASE_URL",
        default="postgresql+asyncpg://postgres:postgres@127.0.0.1:6433/postgres",
    )


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session", autouse=True)
async def engine():
    engine = create_async_engine(TEST_DATABASE_URL, future=True, echo=True)
    yield engine

@pytest.fixture(scope="session", autouse=True)
async def async_session_test(engine):
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    yield async_session


@pytest.fixture(scope="session", autouse=True)
async def run_migrations():
    alembic_cfg = Config("/home/user/Python/Into_the_wild/backend/test_backend/alembic.ini")
    # command.init(alembic_cfg,"/home/user/Python/Into_the_wild/backend/test_backend/migrations")
    command.revision(alembic_cfg, autogenerate=True, message="test running migrations")
    command.upgrade(alembic_cfg, "head")


pytest.fixture(scope="function", autouse=True)
async def clean_tables(engine, async_session_test):
    async with async_session_test() as session:
        async with session.begin():
            for table_name in CLEAN_TABLES:
                with engine.sync_engine.connect() as conn:
                    metadata = conn.run_sync(MetaData)
                    table = conn.run_sync(Table, table_name, metadata, autoload=True)
                    await session.execute(table.delete())


async def _get_test_db():
    try:
        test_engine = create_async_engine(
            TEST_DATABASE_URL, future=True, echo=True
        )

        test_async_session = sessionmaker(
            test_engine, expire_on_commit=False, class_=AsyncSession
        )
        yield test_async_session()
    finally:
        pass


@pytest.fixture(scope="function")
async def client() -> Generator[TestClient, Any, None]:
    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client
