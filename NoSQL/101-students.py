#!/usr/bin/env python3
"""Este módulo lista los alumnos por puntuación."""


def top_students(mongo_collection):
    """
    Retorna todos los estudiantes ordenados por su puntaje promedio.

    Args:
        mongo_collection: Objeto de colección de PyMongo.

    Returns:
        list: Lista de estudiantes ordenados por su puntaje promedio.
    """
    pipeline = [
         {"$addFields": {"averageScore": {"$avg": "$topics.score"}}},
         {"$sort": {"averageScore": -1}}
         ]
    top = mongo_collection.aggregate(pipeline)
    return list(top)