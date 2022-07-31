import logging

import aioredis
import asyncio
import json
import os

import websockets

WEBSOCKET_HOST = os.getenv("WEBSOCKET_HOST", "ws-server")
WEBSOCKET_PORT = os.getenv("WEBSOCKET_PORT", 9999)

LOG_LEVEL_ENV = os.getenv("LOG_LEVEL", "debug")

LOG_LEVEL_MAP = {"debug": logging.DEBUG, "info": logging.INFO}

logging.basicConfig(encoding="utf-8", level=LOG_LEVEL_MAP[LOG_LEVEL_ENV])


async def init_redis():
    redis = aioredis.from_url("redis://redis")
    logging.debug("Redis connection created")
    return redis


async def save_to_redis(redis, tickers):
    async with redis.client() as conn:
        ts = tickers.pop("ts")
        for ticker_name, value in tickers.items():
            await conn.execute_command("TS.ADD", ticker_name, ts, value)

        logging.info(":::SAVED to REDIS, timestamp %s ", ts)


async def ws_connect():
    redis = await init_redis()
    async with websockets.connect(
        f"ws://{WEBSOCKET_HOST}:{WEBSOCKET_PORT}"
    ) as websocket:
        async for message in websocket:
            tickers = json.loads(message)
            await save_to_redis(redis, tickers)


if __name__ == "__main__":
    logging.info("Websocket client started")
    asyncio.run(ws_connect())
