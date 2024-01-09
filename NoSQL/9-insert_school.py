#!/usr/bin/env python3
""" Function that inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs
    Args:
        mongo_collection (collection): collection to insert the document into
        **kwargs (dict): key-value pairs to insert as the document
    Returns:
        inserted document's _id
     """
    return mongo_collection.insert_one(kwargs).inserted_id
