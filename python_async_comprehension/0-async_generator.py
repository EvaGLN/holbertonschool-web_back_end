#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """10 loops asynchronously waiting 1sec yeld random number 0-10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
