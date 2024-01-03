#!/usr/bin/env python3
""" Concurrent Coroutines """

import asyncio
import typing

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Returns a list of all the delays (float values) in ascending order.
    Args:
        n (int): number of times to call wait_random
        max_delay (int): maximum delay to wait for
    Returns:
        list of all delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
