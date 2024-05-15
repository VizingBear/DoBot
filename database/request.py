from database import models
from .database import async_session


async def set_new_product():
    async with async_session() as session:
        pass
