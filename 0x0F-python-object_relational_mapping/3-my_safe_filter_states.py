#!/usr/bin/python3
""" Lists all values in the states tables of a database where name
matches the argument safely
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         database=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = %s\
                    ORDER BY states.id;", (argv[4],))

    [print(state) for state in cursor.fetchall()]
