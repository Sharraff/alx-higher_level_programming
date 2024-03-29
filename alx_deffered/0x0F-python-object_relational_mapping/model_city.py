#!/usr/bin/python3
"""
script for using sqlalchemy to model our models using ORM
"""
from sqlachemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    cities class for use with sqlachemy inherits from sqlachemy
    declarative_base
    """
    __tabe__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
