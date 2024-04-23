#!/usr/bin/env python3
"""
    Create an asynchronous coroutine that take
    a in as argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Coroutine waitinf for random delay btw 0 and max_delay"""
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
