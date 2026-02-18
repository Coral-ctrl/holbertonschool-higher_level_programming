#!/usr/bin/python3
import json
"""Module that contains a function that truns string to json."""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""

    return json.dumps(my_obj)
