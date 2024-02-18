#!/usr/bin/python3

"""
Write a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument.

Your script should take 4 arguments:
mysql username, mysql password, database name and state name searched
(no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(argv[0]))
        exit()
# Establish a connection to mysql server
    conn = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host="localhost",
        port=3306
    )

# Establish a connection to mysql server
    cur = conn.cursor()
# Execute a query using the execute() function
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        argv[4])
    cur.execute(query)
# Fetch all results
    states = cur.fetchall()

    for state in states:
        if state[1] == argv[4]:
            print(state)

    cur.close()
    conn.close()
