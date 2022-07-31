import logging
import asyncio
import os


from utils import init_tickers, calculate_step, init_redis, save_to_redis


LOG_LEVEL_ENV = os.getenv("LOG_LEVEL", "debug")

LOG_LEVEL_MAP = {"debug": logging.DEBUG, "info": logging.INFO}

logging.basicConfig(encoding="utf-8", level=LOG_LEVEL_MAP[LOG_LEVEL_ENV])


async def main():
    redis_conn = await init_redis()
    current_tickers = await init_tickers()
    logging.info("Producing started!")
    while True:
        current_tickers = await calculate_step(current_tickers)
        await save_to_redis(redis_conn, current_tickers)
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
