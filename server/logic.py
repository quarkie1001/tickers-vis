from random import random


async def generate_movement():
    movement = -1 if random() < 0.5 else 1

    return movement


async def calculate_step():
    step_values = [await generate_movement() for _ in range(100)]

    return step_values
