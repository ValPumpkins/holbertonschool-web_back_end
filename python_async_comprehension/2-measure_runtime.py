#!/usr/bin/env python3
""" Measures the total runtime of execution of async_comprehension
in parallel using asyncio.gather
"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures the total runtime
    Returns:
        float: total runtime
    """
    task = [async_comprehension() for _ in range(4)]

    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(*task)

    end_time = asyncio.get_event_loop().time()

    total_time = end_time - start_time

    return total_time
