#!/usr/bin/env python3
""" Creates an asyncio task that waits for a random delay """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Returns an asyncio task
    Args:
        max_delay (int): maximum delay
    Returns:
        asyncio.Task: asyncio task
    """
    return asyncio.create_task(wait_random(max_delay))
