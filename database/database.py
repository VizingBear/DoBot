from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("sqlite+aiosqlite:///db/start_info.db")
async_session = async_sessionmaker(engine, expire_on_commit=True)


class Base(DeclarativeBase):
    pass

