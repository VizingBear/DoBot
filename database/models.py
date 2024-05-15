from sqlalchemy.orm import Mapped, mapped_column

from .database import Base, engine


class UserInfo(Base):
    __tablename__ = "user_info"

    id: Mapped[int] = mapped_column(primary_key=True)


class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)



async def async_create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)