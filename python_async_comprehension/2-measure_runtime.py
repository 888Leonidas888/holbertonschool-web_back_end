#!/usr/bin/env python3
"""Compresión asíncrona y generadores asíncronos."""

from time import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutina que regresa el tiempo de ejecucación
    de la corutina async_comprehesion ejecutada 4 veces.

    Returns:
        float: Tiempo de ejecución de async_comprehension x 4.
    """
    start = time()
    task = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)
    finish = time()
    return finish - start
