#!/usr/bin/python3
"""Time to turn lead into gold"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City, State).join(
            State, City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(city[1].name, city[0].id, city[0].name))

    session.close()
