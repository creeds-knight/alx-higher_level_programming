#!/usr/bin/python3
"""
    A script that takes in the name of a state as an argument and lists
    all cities of that state
"""
import sys
import MySQLdb


def check_state_city(username, password, db_name, state_name):
    """ A script that prints cities in a state """
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=db_name)

        cur = db.cursor()
        querry = "SELECT cities.name FROM cities INNER JOIN states ON\
                cities.state_id = states.id WHERE states.name = %s"
        cur.execute(querry, (state_name,))
        rows = cur.fetchall()
        cities = [row[0] for row in rows]
        print(", ".join(cities))
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error:{e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: <username> <password> <db_name> <state_name>")
        sys.exit(1)
    username, password, db_name, state_name = sys.argv[1:]
    check_state_city(username, password, db_name, state_name)
