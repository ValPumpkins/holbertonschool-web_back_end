#!/usr/bin/env python3

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of all the delays (float values) in ascending order
    Args:
        n (int): number of times to call wait_random
        max_delay (int): maximum delay to wait for
    Returns:
        list of all delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
