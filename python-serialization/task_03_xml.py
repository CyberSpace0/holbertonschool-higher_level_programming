#!/usr/bin/python3
"""Module for XML serialization and deserialization."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for child in root:
        value = child.text

        # Convert back to the appropriate type
        if value == "True":
            value = True
        elif value == "False":
            value = False
        else:
            try:
                value = int(value)
            except (ValueError, TypeError):
                pass

        dictionary[child.tag] = value

    return dictionary
