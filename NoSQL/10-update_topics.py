#!/usr/bin/env python3
""" Function that changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name
    Args:
        mongo_collection (collection): collection to update
        name (str): name of the school to update
        topics (list): list of topics to update to
    Returns:
        updated collection
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
