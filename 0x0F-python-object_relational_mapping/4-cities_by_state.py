#!/usr/bin/python3
"""
    A script to list all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def cities_check(username, password, db_name):
    """ A function to print cities """
    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=db_name)

        cur = db.cursor()
        querry = "SELECT * FROM cities ORDER BY iD ASC"
        rows = cur.execute(querry)
        for row in rows.fetchall():
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database>")
        sys.exit(1)
    username, password, db_name = sy.argv[1:]
    cities_check(username, db_name, db_name)


