#!/usr/bin/python3
"""
    A script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def states(username, password, db_name):
    """ A function to print out the states"""

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE id IN(SELECT MIN(id)\
                 FROM states GROUP BY name) ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    username, passwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    states(username, passwd, db_name)
