#!/usr/bin/python3

"""
Transform a class into a json object
"""

import json


def class_to_json(obj):
    """
    Transform a class into a json object
    """
    return vars(obj)
