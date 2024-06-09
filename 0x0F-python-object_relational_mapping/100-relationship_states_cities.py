#!/usr/bin/python3
""" A module that adds a state based on a relationship
"""
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import sys
from model_state import Base



def relationship_add(username, password, db_name):
    """ A function add state and city"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
            username, password, "3306", db_name))
        Session = sessionmaker(bind=engine)
        session = Session()

        Base.metadata.create_all(engine)

        new_state = State(name="California")
        new_city = City(name="San Francisco", state=new_state)

        session.add_all([new_state, new_city])

        session.commit()

        session.close()
    except SQLAlchemyError as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    relationship_add(username, password, db_name)
