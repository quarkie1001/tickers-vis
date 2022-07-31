import aioredis
import logging
from random import random
import time


async def init_tickers():
    tickers_keys = [f"ticker_{num:02d}" for num in range(100)]
    tickers_dict = dict.fromkeys(tickers_keys, 0)

    return tickers_dict


async def generate_movement():
    movement = -1 if random() < 0.5 else 1

    return movement


async def calculate_step(tickers):
    logging.debug(tickers)
    deltas = [await generate_movement() for _ in range(100)]
    new_values = [x + int(y) for x, y in zip(tickers.values(), deltas)]
    new_dict = {k: v for k, v in zip(tickers.keys(), new_values)}

    return new_dict


async def init_redis():
    redis = aioredis.from_url("redis://redis")
    logging.debug("Redis connection created")
    return redis


async def save_to_redis(redis, tickers):
    async with redis.client() as conn:
        ts = int(time.time())
        for ticker_name, value in tickers.items():
            await conn.execute_command("TS.ADD", ticker_name, ts, value)

        logging.info(":::SAVED to REDIS, timestamp %s ", ts)
