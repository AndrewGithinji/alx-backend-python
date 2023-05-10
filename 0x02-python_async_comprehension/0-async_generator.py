#!/usr/bin/env python3
"""
0x02. Asynchronous Programming
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine will loop 10 times, and each time asynchronously
    wait for 1 second before yielding a random float value in the range
    between 0 and 10, using the random module.
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
