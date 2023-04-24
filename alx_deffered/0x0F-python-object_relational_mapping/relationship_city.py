#!/usr/bin/python3
"""
Created on 19 march 2023
@author: Musharraff Ibrahim
"""
import sqlalchemy
import sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    A new table in to the data base for city representation
    """
    __table__ = "cities"
    id = Column(Integer, primary_key=True)
    name = column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id))
