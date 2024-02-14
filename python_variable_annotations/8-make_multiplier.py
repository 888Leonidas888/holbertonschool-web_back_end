#!/usr/bin/env python3
"""Anotaciones de tipos complejos en Python."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplica un número por el multiplicador dado.
    
    Args:
        multiplier (float): El multiplicador.

    Returns:
        Callable[[float], float]: Una función que toma un flotante
        y devuelve su producto con el multiplicador.
    """
    def multiplier_function(number: float) -> float:
        return number * multiplier
    return multiplier_function
