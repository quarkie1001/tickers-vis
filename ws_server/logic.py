from random import random
import time


async def init_tickers():
    start_timestamp = int(time.time())
    tickers_keys = [f"ticker_{num:02d}" for num in range(100)]
    tickers_dict = dict.fromkeys(tickers_keys, 0)
    tickers_dict["ts"] = start_timestamp

    return tickers_dict

async def generate_movement():
    movement = -1 if random() < 0.5 else 1

    return movement

async def calculate_step(current):
    ts = current.pop("ts")
    deltas = [await generate_movement() for _ in range(100)]
    new_values = [x + int(y) for x, y in zip(current.values(), deltas)]
    new_dict = {k: v for k, v in zip(current.keys(), new_values)}
    new_dict["ts"] = ts + 1

    return new_dict
