#!/usr/bin/python3

"""
Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa:

Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host="localhost",
        port=3306
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    states = cur.fetchall()

    for state in states:
        if state[1][0] == 'N':
            print(state)

    cur.close()
    conn.close()
