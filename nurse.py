import sqlite3
import re

conn = sqlite3.connect("hospital.db")
c = conn.cursor()

# Nurses tasks

def nurse_q1(hcno):
    
    c.execute('SELECT hcno FROM patients p WHERE p.hcno=:hcno;',{'hcno':hcno})
    if not c.fetchone():
        print 'This Patient does not exist in our system'
        
    else:
        c.execute('SELECT c.chart_id FROM charts c, patients p WHERE c.hcno = p.hcno AND c.edate is NULL AND c.hcno=:hcno;', {"hcno":hcno})
        chart = c.fetchone()
    
        if not chart:
            print "This Chart has already been closed"
            
        else:   
            c.execute('UPDATE charts SET edate = datetime() WHERE edate is NULL AND hcno=:hcno;', {"hcno": hcno}) 
            print 'Patient ' + hcno + ' has been discharged.' #, chart number ' + chart +'is now closed'
    
def nurse_q2():
    print "This is the creat chart"