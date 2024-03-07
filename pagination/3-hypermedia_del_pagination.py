#!/usr/bin/env python3
"""Paginación hipermedia resistente a la eliminación."""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Regresa la paginación solicitada, ademas la hipermedia considerando
        la elimanción de los datos.

        Args:
            index(int): Número de página.
            page_size(int): Cantidad de items por página.

        Returns:
            dict: Con la hypermedia de la paginación solictada.
        """
        assert index < len(self.__indexed_dataset), AssertionError

        dict_hyper = {}

        n = 0
        end_index = index + page_size
        next_index = end_index
        data = []

        for i in range(index, end_index):
            item = self.__indexed_dataset.get(i)
            if item is None:
                n += 1
                next_index += 1
            data.append(self.__indexed_dataset.get(i + n))

        dict_hyper['index'] = index
        dict_hyper['next_index'] = next_index
        dict_hyper['page_size'] = len(data)
        dict_hyper['data'] = data
        return dict_hyper
