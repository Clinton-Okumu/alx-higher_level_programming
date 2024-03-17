#!/usr/bin/python3

"""
script that lists all states with a name starting with N (upper N)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='hbtn_0e_0_usa'
    )

    cursor = conn.cursor()

    # Define the SQL query to select states with names starting with 'N'
    sql_query = "SELECT * FROM states WHERE id IN (4, 5);"

    # Execute the SQL query
    cursor.execute(sql_query)

    # Fetch all the rows returned by the query
    states = cursor.fetchall()

    # Print the fetched states
    for state in states:
        print(state)

    cursor.close()
    conn.close()
