#!/usr/bin/env python3
"""Este script actualiza los topics de una escuela."""


def update_topics(mongo_collection, name, topics):
    """
    Actualiza los topics en una colección.

    Args:
        mongo_collection(Collection): Una colección de MongoDB
        name(str): Nombre de la school.
        topics(list): Lista de tareas.
    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
