#!/usr/bin/python3


'''
An sqlalchemy module that creates a declarative base
subclass to which a city database table will be mapped.
'''


from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class City(Base):
    '''
    Subclass of declarative base class
    with class attributes including foreignkey to State class.
    '''
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

    state = relationship("State", back_populates="cities")
