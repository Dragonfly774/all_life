# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute("""SELECT DISTINCT year FROM Films WHERE title LIKE 'X%';""").fetchall()

for i in result:
    print(i[0])
