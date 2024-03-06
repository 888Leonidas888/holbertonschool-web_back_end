#!/usr/bin/env python3
"""Paginación simple."""


def index_range(page, page_size):
    """
    Regresa una tupla con 2 valores; indice inicial
    y final correspondientes a los items a entregar
    de una página.

    Args:
        page(int): Número de página.
        page_size(int): Cantidad de items por página.

    Returns:
        tuple: (int , int)
    """
    finish_index = page * page_size
    start_index = finish_index - page_size
    return (start_index, finish_index)
