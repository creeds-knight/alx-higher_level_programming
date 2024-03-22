#!/usr/bin/python3
"""
    A script that displays all values where a name matches argument
    hbtn_0e_0usa
"""
import sys
import MySQLdb


def state_check(username, password, database, state):
    """
         This function prints all values associated with a state name"
    """
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database)
        cur = db.cursor()
        state_escaped = db.escape_string(state)
        querry = "SELECT * FROM states  WHERE name = _utf8mb4 %s COLLATE\
                  utf8mb4_0900_as_cs ORDER BY id ASC"
        cur.execute(querry, (state, ))
        res = cur.fetchall()
        for state in res:
            print(state)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error:{e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: <username> <password> <database> <state>")
        sys.exit(1)
    state_check(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
