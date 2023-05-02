#!/usr/bin/env python3
"""2. Measure the runtime of concurrent coroutines"""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n(n, max_delay)by running it once.
    Return the average time taken to execute a single coroutine.
    """
    start_time = perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end_time = perf_counter()

    avg_time = (end_time - start_time) / n

    return avg_time
