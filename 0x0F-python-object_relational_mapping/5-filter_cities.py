#!/usr/bin/python3
"""
Script that lists all cities of a specified state from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()

    # Extract city names and join them into a comma-separated string
    city_names = [row[0] for row in rows]
    result = ", ".join(city_names)

    print(result)

    cur.close()
    db.close()
