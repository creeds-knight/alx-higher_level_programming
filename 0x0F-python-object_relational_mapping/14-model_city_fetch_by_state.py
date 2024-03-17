#!/usr/bin/python3
""" A module that lists all State Objects from hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from model_city import City
import sys


def do_join(username, password, db_name):
    """ A function to return objects"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
            username, password, "3306", db_name))
        Session = sessionmaker(bind=engine)
        session = Session()
        cit_st = session.query(City, State).\
            join(State, City.state_id == State.id).order_by(City.id).all()
        for city, state in cit_st:
            print(f"{state.name}: ({city.id}) {city.name}")

        session.close()
    except SQLAlchemyError as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    do_join(username, password, db_name)
