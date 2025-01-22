from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres:postgres@db:5432/postgres"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
async_session = async_sessionmaker(engine, expire_on_commit=False)
