import sqlite3
import re

conn = sqlite3.connect("hospital.db")
c = conn.cursor()

# Nurses tasks

def nurse_q1(c, connection):

    print 'If you are closing a patient file, please enter patients Healthcare Number'
    hcno = raw_input('Enter hcno: ')
    
    c.execute('UPDATE charts SET edate = datetime() WHERE edate is NULL;') 
    