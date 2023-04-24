#!/usr/bin/python3
"""
created on 19 march 2023
@uthor: Musharraff Ibrahim
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    A new table in to the database for state representaion
    """
    __table__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("city", backref="state")
