#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
"""
import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    db = MySQLdb.connect(user=args[0], password=args[1],
                         database=args[2], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states;""")

    for state in cursor.fetchall():
        print(state)
