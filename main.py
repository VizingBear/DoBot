import asyncio
import logging
import sys

from bot.bot import dp, bot
from database.models import async_create_tables


async def main() -> None:
    await async_create_tables()

    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
