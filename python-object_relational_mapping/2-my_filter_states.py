#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states table where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query using format (vulnerable to SQL injection)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
