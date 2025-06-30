#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter a"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete State objects containing 'a'
    states_to_delete = session.query(State).filter(State.name.contains('a')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    # Close session
    session.close()
