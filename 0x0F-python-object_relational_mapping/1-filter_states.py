#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    db = MySQLdb.connect(user=args[0], password=args[1],
                         database=args[2], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY states.id;""")

    [print(state) for state in cursor.fetchall()]
