#!/usr/bin/env python3
"""Execute multiple coroutines concurrently with async"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for n random delays between 0 and max_delay seconds (inclusive).
    Return a sorted list of the amount of time waited for each delay.
    """

    tasks = (wait_random(max_delay) for i in range(n))
    

    results = await asyncio.gather(*tasks)
    

    return sorted(results)
