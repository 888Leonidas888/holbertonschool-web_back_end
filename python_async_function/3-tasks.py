#!/usr/bin/env python3
"""Python asíncrono: Taks"""

import asyncio
from typing import Any


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Regrese una Task.

        Args:
            max_delay (int): Máximo tiempo de espera.

        Retunrs:
            asyncio.Task : Regresa una Task.
    """
    return asyncio.create_task(wait_random(max_delay))
