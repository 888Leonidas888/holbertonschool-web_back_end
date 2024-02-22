#!/usr/bin/env python3
"""Comprensión asíncrona y generadores asíncronos."""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutotina que recupera 10 números aleatorios de forma asíncrona.

    Utiliza una comprensión asíncrona sobre la coroutina async_generator
    para recolectar 10 números random.

    Retunrs:
        List[float]: Lista de 10 números aleatorios
    """
    return [i async for i in async_generator()]
