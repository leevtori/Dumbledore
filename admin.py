#!/usr/bin/python
import sqlite3
import re

conn = sqlite3.connect('hospital.db')
c = conn.cursor()
#---------------------------------------------------------------  
def admin_query1():
    from_date = "" 
    while not re.match('\d{4}[/.-](\d{2}[/.-](\d{4})$',from_date):
        from_date = raw_input("Please indicate start date with format 'yyyy-mm-dd' (e.g. 2010-01-31)")
        
        
    to_date = ""
    while not re.match('\d{4}[/.-](\d{2}[/.-](\d{4})$',from_date):
        to_date = raw_input("Please indicate end date with format 'yyyy-mm-dd'(e.g. 2010-02-20)")
       


    c.execute("select staff.name, medications.drug_name,SUM(medications.amount) AS total_amount_prescribed from staff, medications where julianday(medications.mdate)>=julianday(:from_date) and julianday(medications.mdate)<=julianday(:to_date) and medications.staff_id=staff.staff_id GROUP BY medications.drug_name;",{"from_date":from_date, "to_date":to_date})

    result = c.fetchall()
    for line in result:
        print(line)
        print('\n')
#---------------------------------------------------------------  
def admin_query2():
    return
#---------------------------------------------------------------  
def admin_query3():
    diagnosis=" "
    while diagnosis.isalpha() == False:
        diagnosis = raw_input("Enter diagnosis name: ")

    c.execute("select medications.drug_name as possible_medications from medications, diagnoses where diagnoses.diagnosis= :diagnosis and julianday(medications.mdate)>=julianday(diagnoses.ddate) group by medications.drug_name order by count(*) DESC;",{"diagnosis":diagnosis})
    
    result_list = c.fetchall()
    for i in range(len(result_list)):
        print(result_list[i])

#---------------------------------------------------------------        
def admin_query4():
    drug=" "
    while drug.isalpha() == False:
        drug = raw_input("Enter drug name: ")

    c.execute("select diagnoses.diagnosis as previous_diagnoses from diagnoses,medications where medications.drug_name=:drug and julianday(diagnoses.ddate)<julianday(medications.mdate) group by previous_diagnoses order by AVG(medications.amount);",{"drug":drug})

    result_list = c.fetchall()
    for i in range(len(result_list)):
        print(result_list[i])
    

#MAIN
admin_query3()
admin_query4()
conn.close()



    
    
