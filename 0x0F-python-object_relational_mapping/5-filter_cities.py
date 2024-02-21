#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_4_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
    )

    state_name = sys.argv[4]

    cur = db.cursor()
    cur.execute("""
                SELECT cities.name FROM cities
                INNER JOIN states ON states.id=cities.state_id
                WHERE states.name LIKE %s
                """, (state_name, ))
    rows = cur.fetchall()
    cities = ", ".join(row[0] for row in rows)
    print(cities)
    cur.close()
    db.close()
