#!/usr/bin/python3
""" A module that adds a state hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import sys


def add_state(username, password, db_name):
    """ A function to add a state"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
            username, password, "3306", db_name))
        Session = sessionmaker(bind=engine)
        session = Session()
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        states = session.query(State).order_by(State.id).filter(
                State.name == "Louisiana")
        for state in states:
            print(f"{state.id}")

        session.close()
    except SQLAlchemyError as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    add_state(username, password, db_name)
