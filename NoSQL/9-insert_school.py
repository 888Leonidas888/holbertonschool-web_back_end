#!/usr/bin/env python3
"""Inserta un nuevo documento en Python."""


def insert_school(mongo_collection, **kwargs):
    """
    Inserta un nuevo documento en una colección.

    Args:
        mongo_collection(Collection): Colección de MongoDB.

    Retunrs:
        str: _id generado para ese documencto.
    """
    id = mongo_collection.insert_one(kwargs).inserted_id
    return id
