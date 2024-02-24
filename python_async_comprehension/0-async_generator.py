#!/usr/bin/env python3
"""Comprensión asíncrona y generadores asíncronos."""

import asyncio
from typing import AsyncGenerator
from random import uniform


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Coroutina que genera valores aleatorios entre 0 y 10
    de manera asíncrona.

    Cada iteración espera 1 segundo para producir el siguiente número.

    Yields:
        float: Float entre 0 y 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
