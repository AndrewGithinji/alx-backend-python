#!/usr/bin/env python3
"""A basic async function that waits for a random amount of time"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random amount of time between 0 and max_delay seconds.
    Return the amount of time waited.
    """
    # Generate a random delay between 0 and max_delay
    delay = random.uniform(0, max_delay)

    # Wait for the random delay using asyncio.sleep()
    await asyncio.sleep(delay)

    # Return the amount of time waited
    return delay
