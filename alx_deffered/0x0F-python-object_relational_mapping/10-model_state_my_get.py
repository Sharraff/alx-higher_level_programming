#!/usr/bin/python3
"""
created on 19 march 2023
@author: Musharraff Ibrahim
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print("Usage: {} username password database".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    engine = create_engine('mysql+mysql://{}:{}@localhost/{}'
            .format(username, password, data))
    # create custom session object class from data engine
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    session = Session()
    states = session.query(State).filter(State.name == state_name)\
            .order_by(State.id)
    if states is not None and states.count() > 0:
        for state in states:
            print('{}: {}'.format(state.id))
    else:
        print('Not found')
