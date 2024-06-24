#!/usr/bin/python3


'''
A sqlalchemy module that connects to mysql database,
creates a session, and prints in a formatted output,
associated data in the states' and cities' tables.
'''


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, declarative_base
from model_state import Base, State
from model_city import City

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3],
        pool_pre_ping=True
        ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj_list = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()
    for row in obj_list:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
