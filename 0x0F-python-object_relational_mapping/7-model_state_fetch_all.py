#!/usr/bin/python3
""" A module that lists all State Objects from hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import sys


def list_objects(username, password, db_name):
    """ A function to return objects"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
            username, password, "3306", db_name))
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")

        session.close()
    except SQLAlchemyError as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    list_objects(username, password, db_name)
