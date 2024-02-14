#!/usr/bin/env python3
"""Un objeto iterable."""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Esta función recibe un iterable y regresa una lista de tuplas

    Args:
        lst (Iterable): Este parámetro es un iterable.

    Returns:
        List[Tuple[Sequence, int]] : Lista de tuplas.
    """
    return [(i, len(i)) for i in lst]
