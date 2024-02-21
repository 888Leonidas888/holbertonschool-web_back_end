#!/usr/bin/env python3
"""Python asíncrono: medir el tiempo de ejecución."""

from time import time
import warnings

warnings.filterwarnings('ignore', category=RuntimeWarning)

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Mide el tiempo promedio de ejecución de cada tarea.

        Args:
            n (int): Las veces que debe ejecutar la tarea.
            max_delay (int): Límite superior de random.

        Returns:
            float : Tiempo promedio tiempo_total / n
    """
    start = time()
    wait_n(n, max_delay)
    finish = time()
    return (finish - start) / n
