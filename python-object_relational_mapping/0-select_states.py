#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


if __name__ == "__main__":
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Close cursor and database connection
    cursor.close()
    db.close()
