#!/usr/bin.python3

"""
Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql
username, mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    #Establish a connection to mysql server
    con = MySQLdb.connect(
        user=username,
        passwd=password,
        database=database,
        host="localhost",
        port=3306
        )
    #create a cursor object to execute queries
    cur = con.cursor()
    #Execute a query using the execute() function
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    #Fetch all results
    results = cur.fetchall()

    for state in results:
        print(state)
    #close cursor and connection
    cur.close()
    con.close()
