#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the query to select all cities with their respective states
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Print the retrieved rows
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()
