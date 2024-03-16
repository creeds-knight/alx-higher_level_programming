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
        querry = "SELECT id, name FROM states WHERE id IN (SELECT MIN(id)\
                    FROM states GROUP BY name) AND name = %s\
                    ORDER BY id"
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
