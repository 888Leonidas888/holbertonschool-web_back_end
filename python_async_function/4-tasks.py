#!/usr/bin/env python3
"""Python asíncrono: Tasks 2"""


from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Lamzamos varias tareas en paralelo.

        Args:
            n (int): Las veces que debe ejecutar la tarea.
            max_delay (int): Límite superior para random.

        Returns:
            List[float]: Una lista con tiempo de espera.
    """
    temp_list = []
    for _ in range(n):
        temp_list.append(await task_wait_random(max_delay))
    return sorted(temp_list)
