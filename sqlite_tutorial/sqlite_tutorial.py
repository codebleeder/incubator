#!/usr/bin/env python
__author__ = 'sharad'
import sqlite3
# connection object
connection = sqlite3.connect('example.db')
# cursor object
c = connection.cursor()

# create table
c.execute(''' CREATE TABLE stocks
              (date text, symbol text, price real)''')

# insert row
c.execute('''INSERT INTO stocks VALUES('07-08-2015', 'APL', 76.7)''')
c.execute('''INSERT INTO stocks VALUES('07-08-2015', 'FB', 40)''')

connection.commit()
connection.close()

