#!/usr/bin/env python3
"""Este módulo usa pymongo para listar los documentos."""

from typing import List, Dict, Any
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """
    Lista todos los documentos en una colección MongoDB.

    Args:
        mongo_collection(Collection): Objeto de colección de PyMongo.

    Returns:
        List[Dict[str, Any]]: Una lista de documentos de la colección recibida.
    """
    documents: List[Dict[str, Any]] = []

    cursor = mongo_collection.find()
    documents = [document for document in cursor]
    return documents
