#!/usr/bin/env python3
"""function that measures the total execution time for wait_n(n, max_delay),"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average time per call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter() - start_time
    total_time = end_time / n
    return total_time
