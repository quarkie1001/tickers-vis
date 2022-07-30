import logging

import aioredis
import asyncio
import json
import os

import websockets

WEBSOCKET_HOST = os.getenv("WEBSOCKET_HOST", "ws-server")
WEBSOCKET_PORT = os.getenv("WEBSOCKET_PORT", 9999)


LOG_LEVEL_ENV = os.getenv("LOG_LEVEL", "debug")

LOG_LEVEL_MAP = {"debug": logging.DEBUG,
                 "info": logging.INFO}

logging.basicConfig(encoding='utf-8', level=LOG_LEVEL_MAP[LOG_LEVEL_ENV])

async def init_redis():
    redis = aioredis.from_url("redis://redis")
    logging.debug("Redis connection created")
    return redis

async def save_to_redis(redis, step_number, tickers):
    async with redis.client() as conn:
        # for ticker_name, ticker_value in tickers.items():
        #     await conn.hsetnx(ticker_name, step_number, ticker_value) # add ticker price for step in it doesn't exists
        for ticker_name, ticker_value in tickers.items():
            await conn.rpush(ticker_name, ticker_value)
        logging.info("STEP %s SAVED to REDIS", step_number)



async def ws_connect():
    redis = await init_redis()
    step_number = 0
    async with websockets.connect(f"ws://{WEBSOCKET_HOST}:{WEBSOCKET_PORT}") as websocket:
        async for message in websocket:
            tickers = json.loads(message)
            # logging.info(tickers)
            await save_to_redis(redis, step_number, tickers)
            step_number += 1
            #await load_from_redis(redis)



if __name__ == '__main__':
    logging.info(f"Websocket client started")
    asyncio.run(ws_connect())
