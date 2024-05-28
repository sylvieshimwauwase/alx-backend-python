#!/usr/bin/env python3
"""function to measure runtime in parallel"""

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure runtime of async comprehension"""
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return end_time - start_time
