#!/usr/bin/python3

'''
A sqlalchemy module that connects to mysql database,
creates a session, queries all rows of the States table and
prints a formated output of objects that match the pattern.
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
    state_list = session.query(State).filter(
                    State.name.like('%a%')).order_by(State.id)
    for row in state_list:
        print("{}: {}".format(row.id, row.name))
