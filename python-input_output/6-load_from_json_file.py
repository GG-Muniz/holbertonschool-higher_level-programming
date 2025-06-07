#!/usr/bin/python3
"""Module that contains a function to load object from JSON file."""
import json


def load_from_json_file(filename):
    """Create an Object from a JSON file.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        The object loaded from the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
