#!/usr/bin/env python3
"""Python asíncrono."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Lamzamos varias tareas en paralelo."""
    temp_list = []
    for i in range(n):
        temp_list.append(await wait_random(max_delay))
    return sorted(temp_list)
