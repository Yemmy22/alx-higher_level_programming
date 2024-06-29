#!/usr/bin/python3

'''
An sqlalchemy module that creates a declarative base
subclass to which a state database table will be mapped.
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    '''
    Subclass of declarative base class
    with class attributes.
    '''
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
