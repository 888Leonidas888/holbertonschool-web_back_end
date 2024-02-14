#!/usr/bin/env python3
"""Anotaciones en Python para tipos complejos."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Suma una lista de float.

    Args:
        input_list (list[float]): Una lista de floats.

    Returns:
        float : La suma de input_list
    """
    return float(sum(input_list))
