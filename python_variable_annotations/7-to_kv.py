#!/usr/bin/env python3
"""Anotaciones en Python de tipos complejos."""


from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Union[str, float]:
    """Eleva al cuadrado el segundo argumento.

    Args:
        k (str): Primer argumento.
        v (int | float): segundo argumento.

    Returns:
        tupla : Regresa (k , v ** 2)
    """
    return k, v ** 2
