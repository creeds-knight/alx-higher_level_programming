#!/usr/bin/env python3
"""
    A script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb


def states():
    """ A function to print out the states"""

    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd="root", db="hbtn_0e_0_usa", charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states")
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    states()
