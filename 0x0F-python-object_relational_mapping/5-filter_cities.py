#!/usr/bin/python3
""" Lists all cities of a state passed as argument.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         database=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    WHERE states.name = %s\
                    ORDER BY cities.id;", (argv[4],))

    print(", ".join([city[0] for city in cursor.fetchall()]))
