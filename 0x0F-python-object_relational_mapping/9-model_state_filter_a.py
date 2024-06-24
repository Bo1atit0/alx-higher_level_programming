#!/usr/bin/python3

"""
Write a script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa

Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
- from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}:@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    ))

    Base.metadata.create_all(engine)
    # create session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # query all state objects that contain letter a
    a_states = session.query(State).filter(State.name.like(
        '%a%')).order_by(State.id).all()

    # print results
    for state in a_states:
        print("{:d}: {:s}".format(state.id, state.name))

    # close session
    session.close()
