import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database import Base

test_engine = create_async_engine("postgresql+psycopg://postgres:postgres@db:5432/test", future=True, echo=False)

TestSessionLocal = async_sessionmaker(
    bind=test_engine,
    expire_on_commit=False,
)


async def override_get_session() -> AsyncSession:
    async with TestSessionLocal() as session:
        yield session


async def setup_test_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def teardown_test_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def initialize_test_db():
    await setup_test_db()
    yield
    await teardown_test_db()
