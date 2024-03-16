#!/usr/bin/python3
""" A module that prints the first state from hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import sys


def first_state(username, password, db_name):
    """ A function to print the first state"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
            username, password, "3306", db_name))
        Session = sessionmaker(bind=engine)
        session = Session()
        first = session.query(State).order_by(State.id).first()
        if first:
            print(f"{first.id}: {first.name}")
        else:
            print("Nothing")

        session.close()
    except SQLAlchemyError as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    first_state(username, password, db_name)
