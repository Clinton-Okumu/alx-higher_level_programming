#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
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

    # Execute the query to select cities of the specified state
    cursor.execute("SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Extract city names from the result set
    cities = [row[0] for row in rows]

    # Print the retrieved city names
    print(", ".join(cities))

    # Close cursor and connection
    cursor.close()
    conn.close()
