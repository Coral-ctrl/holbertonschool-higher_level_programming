#!/usr/bin/python3
"""
Module that contains functions for serialization and deserialization
using XML as an alternative format to JSON/
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This will take a Python dictionary and a filename as parameters.
    It should serialize the dictionary into XML and save it to the
    given filename.
    """
    # Create root element
    root = ET.Element("data")

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = Et.SubElement(root, key)
        child.text = str(value)

    # Create tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """
    This will take a filename as its parameter, read the XML data from
    that file, and return a deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            result[child.tag] = child.text

        return result

    except (ET.ParseError, FileNotFoundError, OSError):
        return None
