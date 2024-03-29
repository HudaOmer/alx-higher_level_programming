#!/usr/bin/python3
"""lists all City objects from the database given"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
