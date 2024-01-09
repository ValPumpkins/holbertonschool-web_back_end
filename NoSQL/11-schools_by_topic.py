#!/usr/bin/env python3
""" Function that returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Function that returns the list of school having a specific topic
    Args:
        mongo_collection: pymongo collection object
        topic: topic to be searched
    Returns:
        list of school having the topic
    """
    return mongo_collection.find({"topics": topic})
