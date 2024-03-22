#!/usr/bin/python3
"""
    A script that lists all states with a name starting with N from
    hbtn_0e_0usa
"""
import sys
import MySQLdb


def start_with_N(username, password, database):
    """
         This function prints unique states that start with "N"
    """
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                     COLLATE utf8mb4_0900_as_cs ORDER BY id ASC")
        res = cur.fetchall()
        for state in res:
            print(state)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error:{e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database>")
        sys.exit(1)
    username, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    start_with_N(username, passwd, db)
