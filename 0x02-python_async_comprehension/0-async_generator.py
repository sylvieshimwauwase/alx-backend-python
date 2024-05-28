#!/usr/bin/env python3
"""function to create async generators"""

import asyncio
import random


async def async_generator():
    """generator that yields random numbers between 0 and 10 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
