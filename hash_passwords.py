# hashes the passwords already stored in plaintext in database.

import sqlite3
import hashlib

conn =	sqlite3.connect('hospital.db')
c = conn.cursor()

c.execute("SELECT staff_id, password from staff;")

info=c.fetchall()

for i in range (len(info)):
    staff_id = info[i][0]
    if not info[i][0]:
        continue
    staff_id = staff_id
    password = info[i][1]
    password = hashlib.sha224(password).hexdigest()

    c.execute("UPDATE staff SET password = :password WHERE staff_id = :staff_id", {"password":password, "staff_id":staff_id})

conn.commit()
conn.close()
