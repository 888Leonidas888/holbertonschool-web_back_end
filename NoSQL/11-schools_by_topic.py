#!/usr/bin/env python3
"""Regresa una lista de escuelas con un tema especifico."""


def schools_by_topic(mongo_collection, topic):
    """
    Hace una búsqueda en la colección, de acuerdo al valor de un campo.

    Args
        mongo_collection(Collection): Una colección de MongoDB.
        topic(str): Tema a buscar dentro de topics.

    Returns
        list: Regresa una lista los documentos que tienen el "topic"
            especificado.
    """
    schools = mongo_collection.find({"topics": topic})
    return schools
