#!/usr/bin/env python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Gather command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor object
    cursor = conn.cursor()

    # Define SQL query with user input
    sql_query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC;"

    # Execute the SQL query
    cursor.execute(sql_query, (state_name,))

    # Fetch all the rows returned by the query
    states = cursor.fetchall()

    # Print the fetched states
    for state in states:
        print(state)

    # Close cursor and connection
    cursor.close()
    conn.close()
