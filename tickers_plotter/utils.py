import time

import redis


def init_redis_conn():
    conn = redis.from_url("redis://redis", decode_responses=True)
    conn.set("current_ticker", "ticker_00")

    return conn

def load_values(redis, ticker_name):
    current_ts = int(time.time()) + 1
    values = redis.execute_command(
        "TS.RANGE", ticker_name, current_ts - 10000, current_ts
    )

    return values

def get_ticker_names():
    ticker_names = [f"ticker_{num:02d}" for num in range(100)]

    return ticker_names
