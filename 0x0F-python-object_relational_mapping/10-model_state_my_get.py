#!/usr/bin/python3
""" A module that prints State Objects with name passed from hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import sys


def name_passed(username, password, db_name, name):
    """ A function to print  objects of name passed"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
            username, password, "3306", db_name))
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).order_by(State.id).filter(
                State.name == name).all()
        if len(states) > 0:
            for state in states:
                print(f"{state.id}")
        else:
            print("Not found")

        session.close()
    except SQLAlchemyError as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: <username> <password> <database name>")
        sys.exit(1)

    username, password, db_name, name = sys.argv[1:]
    name_passed(username, password, db_name, name)
