#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         database=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id;")

    [print(city) for city in cursor.fetchall()]
