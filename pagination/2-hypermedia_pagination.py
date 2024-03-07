#!/usr/bin/env python3
""""Paginación de Popular_Baby_Name.csv"""

import csv
import math
from typing import List, Dict, Any

index_range = __import__('0-simple_helper_function').index_range


def validar_entero_positivo(valor: int) -> None:
    """Valida que el valor sea un entero positivo."""
    assert isinstance(valor, int), AssertionError
    assert valor > 0, AssertionError


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Entrega un un slice con la paginación solicitada.

        Args:
            page(int): Número de página.
            page_size(int): Cantidad de items a devolver.

        Returns:
            list: [:] Un slice con la items solicitados.
        """

        validar_entero_positivo(page)
        validar_entero_positivo(page_size)

        star_index, end_index = index_range(page, page_size)

        return self.dataset()[star_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        # def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Regresa un diccionario con los links referentes a la paginación

        Args:
            page(int): Número de página.
            page_size(int): Cantidad de items a devolver.

        Returns:
            dict: Diccionario con los hypermedias.
        """
        total_pages = (len(self.dataset()) + page_size - 1)//page_size
        data = self.get_page(page, page_size)
        next_page = page + 1 if 1 <= page < total_pages else None
        prev_page = page - 1 if 2 <= page <= total_pages else None
        page_size = page_size if data else 0

        hypermedia = {}
        hypermedia['page_size'] = page_size
        hypermedia['page'] = page
        hypermedia['data'] = data
        hypermedia['next_page'] = next_page
        hypermedia['prev_page'] = prev_page if page_size > 0 else page - 1
        hypermedia['total_pages'] = total_pages
        return hypermedia
