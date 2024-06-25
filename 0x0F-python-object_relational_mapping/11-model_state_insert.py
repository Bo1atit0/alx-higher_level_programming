#!/user/bin/python

"""
Write a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa

Your script should take 3 arguments:
mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Print the new states.id after creation
Your code should not be executed when imported

"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    # Check if command line has the required number of args
    if len(argv) != 4:
        print("Usage:{} <username> <password> <database name>"
              .format(argv[0]))
        exit()

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
