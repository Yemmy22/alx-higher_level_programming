#!/usr/bin/python3


'''
A sqlalchemy module that connects to mysql database,
creates a session, and inserts
associated data in the state's and citie's tables.
'''


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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
    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    session.add_all([new_state, new_city])
    session.commit()
    session.close()
