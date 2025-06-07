#!/usr/bin/env python3
"""Module for XML serialization and deserialization."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to XML format.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML data.
    """
    # Create root element
    root = ET.Element("data")

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML data from a file to a Python dictionary.

    Args:
        filename (str): The filename to read the XML data from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct dictionary from XML elements
    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
