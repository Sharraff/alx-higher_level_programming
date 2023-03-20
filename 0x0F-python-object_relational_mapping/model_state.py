#!/usr/bin/python3
"""
created on 19 march 2023
@author: Musharraff Ibrahim
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    state class for use with sqlalchemy inheris from sqlalchemy
    declarative
    """
    __table__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
