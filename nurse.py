import sqlite3
import re

conn = sqlite3.connect("hospital.db")
c = conn.cursor()

# Nurses tasks

def nurse_q1(hcno):
    print "This is the close chart"

    print 'If you are closing a patient file, please enter patients Healthcare Number'
    hcno = raw_input('Enter hcno: ')
    
    c.execute('UPDATE charts SET edate = datetime() WHERE edate is NULL;') 
    
    
def nurse_q2():
    print "This is the creat chart"