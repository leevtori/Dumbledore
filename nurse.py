import sqlite3
import re
import random
import string
from authentication import *


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
            print 'Patient ' + hcno + ' has been discharged.' 
 
#Create a new chart for a patient at the time of admission to the hospital. 
#At that point in time, the adate is filled with the current date and time, and 
#the edate is filled with a NULL value, indicating an "open" chart. Before 
#creating a new chart, the system should check whether there is already an open 
#chart for that patient, and if so, provide the options to either close this 
#chart before creating a new one, or not creating a new one. When creating a 
#new chart, the system also must provide the functionality to add the patient 
#information, if the patient information is not already in the system 
#(from a previous stay in the hospital).
    
def nurse_q2():
    patient = raw_input('Please enter your HCNO: ')
    
    # check if admitted date is filled in 
    c.execute('SELECT hcno FROM charts WHERE hcno=:hcno AND adate is not NULL;',{'hcno':patient}) 
    charts = c.fetchall()
    
    if len(charts) == 0:
        create_patient(patient)
    
    else:
        # check if chart is open
        c.execute('SELECT hcno FROM charts WHERE hcno=:hcno AND edate is NULL;', {'hcno':patient})
        chart = c.fetchone()
        if not chart: # empty query, means edate is full, already closed 
            create_chart(patient)
        else:
            # query found something, there is an open chart
            print 'You appear to have an open chart already, would you like to close this chart?'
            answer = raw_input("Please select Y or N: ")
            if answer == 'Y':
                c.execute('UPDATE charts SET edate = datetime() WHERE edate is NULL AND hcno=:hcno;', {"hcno": patient})
                create_chart(patient)
            else: # N
                pass
        
    
def create_patient(patient):
    print "You don't appear to be in our system, let's create a new account for you\n"
    name = raw_input("Enter your name: ")
    age = raw_input("Enter your age group: ")
    address = raw_input("Enter your address: ")
    phone = raw_input("Enter your phone number: ")
    emerg = raw_input("Enter your emergency contact number :")
        
    c.execute("INSERT INTO patients VALUES('{0}','{1}','{2}','{3}','{4}','{5}');".format(patient, name, age, address, phone, emerg))  
    print 'You are now in our system'
    return

def create_chart(patient):
    c_id = (''.join(random.choice(string.digits) for i in range(3)))
    c.execute("INSERT INTO charts VALUES ('{0}', '{1}', datetime('now'), '{2}');".format(c_id, patient, 'NULL'))
    return

# 3. same as doctors 1

def get_chart():
    patient = raw_input("Enter patient health care number or 0 to exit: ")

    while not patient.isdigit():
        patient = raw_input("Invalid number. Enter patient health care number or 0 to exit: ")

    if patient == '0': return

    list_charts(patient)
    chart_num = raw_input("Enter chart id to view chart or '0' to exit: ")
    while not chart_num.isdigit():
        chart_num = raw_input("Invalid number. Enter chart id to view chart or '0' to exit: ")
    if chart_num == '0': return

    list_entries(chart_num, patient)
    return

def list_charts(patient):
    c.execute("SELECT chart_id, edate FROM charts WHERE hcno = :hcno ORDER BY adate;", {"hcno":patient})
    charts = c.fetchall()
    if not charts:
        print ("No charts found for patient.")
        return
    for chart in charts:
        if not chart[1]:
            status = 'Open'
        else:
            status = 'Closed'
        print 'Chart #' + chart[0] + ':' + status
    return

def list_entries(chart_id, patient):
    c.execute("SELECT * FROM (SELECT staff_id, symptom, obs_date from symptoms WHERE chart_id = :chart_id AND hcno = :patient UNION SELECT staff_id, drug_name, mdate FROM medications WHERE chart_id = :chart_id AND hcno = :patient UNION SELECT staff_id, diagnosis, ddate FROM diagnoses WHERE chart_id = :chart_id AND hcno = :patient) ORDER BY obs_date ;", {"chart_id":chart_id, "patient":patient})
    entries = c.fetchall()
    if not entries:
        print "no entries found."
    for entry in entries:
        print " ".join(entry)
    return

# 4, Same as Doctors 2

def add_line():
    patient = raw_input("Enter patient HCN: ")
    chart = raw_input("Enter chart ID: ")

    c.execute("SELECT chart_id FROM charts WHERE edate IS NULL AND chart_id = :chart AND hcno = :patient ;",{"chart":chart, "patient":patient})
    if not c.fetchone():
        print "Chart does not exist or is not open."
        return

    else:
        content = raw_input("Enter the content of the chart: ")
        c.execute("INSERT INTO symptoms VALUES ('{0}', '{1}' , '{2}' , datetime('now') , '{3}' ) ;".format (patient, chart, user[1], content) )