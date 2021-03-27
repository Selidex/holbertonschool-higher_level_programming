#!/usr/bin/python3
"""Time to turn lead into gold"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    i = 0
    for state in session.query(State).filter(State.name == argv[4]):
        i = 1
        print("{}".format(state.id))
    if i == 0:
        print("Not found")
