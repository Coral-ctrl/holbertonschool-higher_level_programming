#!/usr/bin/python3
"""Module that contains a function converting CSV Data to JSON Format"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Takes the CSV filename as its parameter and writes the
    JSON data to data.json.
    """

    try:
        data_list = []

        # Open and read CSV file
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        # Write JSON data to data,json
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError):
        return False
