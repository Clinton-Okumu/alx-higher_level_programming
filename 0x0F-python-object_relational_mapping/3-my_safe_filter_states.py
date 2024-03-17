#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But this time, write one that
is safe from MySQL injections!
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

    # Execute the query safely
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(query, (argv[4],))

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Print the retrieved rows
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()
