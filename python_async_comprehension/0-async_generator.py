#!/usr/bin/env python3
""" Async generator """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ Async generator function
    Args:
        None
    Yield:
        float: random number between 0 and 10
    """
    for index in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
