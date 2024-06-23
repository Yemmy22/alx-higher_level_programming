#!/usr/bin/python3

'''
A sqlalchemy module that connects to mysql database,
creates a session, updates the database with a new state object
and prints its id attribute.
'''

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, declarative_base
from model_state import Base, State
from sqlalchemy import Column, Integer, String

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_Louisiana = State(name="Louisiana", id="6")
    session.add(state_Louisiana)
    state_id = session.query(State).filter_by(name="Louisiana").first()
    print(state_Louisiana.id)
    session.commit()
