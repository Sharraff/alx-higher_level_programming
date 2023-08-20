#!/usr/bin/python3
""" Script that lists all State objects from the database hbtn_0e_6_usa """

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print(f'{state.id}')
    else:
        print("Not found")
    session.close()