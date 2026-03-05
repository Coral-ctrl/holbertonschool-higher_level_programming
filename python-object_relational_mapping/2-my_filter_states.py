#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    search = sys.argv[4]  # Store argument as a Python variable

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object that sends SQL commands and receives results
    cursor = db.cursor()
    # Execute query
    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(search)
    )
    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Close cursor and database connection
    cursor.close()
    db.close()
