#!/usr/bin/python3

"""
Write a script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa

Your script should take 4 arguments:
mysql username, mysql password, database name
and state name to search (SQL injection free)
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
You can assume you have one record with the state name to search
Results must display the states.id
If no state has the name you searched for, display Not found
Your code should not be executed when imported
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    if len(argv) != 5:
        print("Usage:{} <username> <password> <database> <state name>"
              .format(argv[0]))
        exit()

    # create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
            )
    Base.metadata.create_all(engine)

    # create session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the State Objects with the specified name searched for
    state_name = argv[4]
    query = session.query(State).filter(
        State.name == state_name).first()

    # Displaying the results
    if query:
        print("{:d}".format(query.id))
    else:
        print("Not found")

    # Closing the session
    session.close()
