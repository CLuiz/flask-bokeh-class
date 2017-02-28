import csv
import sqlite3

def drop_table():
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        c.execute('DROP TABLE if EXISTS greenhouse')
    return True


def create_db():
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        c.execute('CREATE TABLE greenhouse (time REAL, temp REAL)')
    return True

def seed():
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        with open('data.dat') as data:
            reader = csv.reader(data)
            for row in reader:
                c.execute('INSERT INTO greenhouse VALUES(?, ?)', row)
    pass
    

if __name__ == '__main__':
    drop_table()
    create_db()
    seed()
