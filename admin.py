
import sqlite3
import re

conn = sqlite3.connect('hospital.db')
c = conn.cursor()
#---------------------------------------------------------------  
def admin_query1():
    print('List for each doctor the name and the total amount of each drug that the doctor prescribed in a specified period of time.')

    from_date = "" 
    to_date = " "

    #regular expression from http://www.regular-expressions.info/dates.html
    while not re.match('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',from_date):
        from_date = raw_input("Please indicate START DATE with format 'yyyy-mm-dd' (e.g. 2010-01-31): ")
        
    to_date = ""
    while not re.match('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',to_date):
        to_date = raw_input("Please indicate END DATE with format 'yyyy-mm-dd'(e.g. 2010-02-20): ")
       
    c.execute("select staff.name, medications.drug_name,SUM(medications.amount) AS total_amount_prescribed from staff, medications where datetime(medications.mdate)>=datetime(:from_date) and datetime(medications.mdate)<=datetime(:to_date) and medications.staff_id=staff.staff_id GROUP BY medications.drug_name;",{"from_date":from_date, "to_date":to_date})

    result_list = c.fetchall()
    for i in range(len(result_list)):
        print(result_list[i])

    print('')
    print('')

#---------------------------------------------------------------  
def admin_query2():
    print("For each category of drugs, list the total amount prescribed for each drug in that category in a specified period of time.")

    from_date = "" 
    to_date = " "

    #regular expression from http://www.regular-expressions.info/dates.html
    while not re.match('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',from_date):
        from_date = raw_input("Please indicate START DATE with format 'yyyy-mm-dd' (e.g. 2010-01-31): ")

    to_date = ""
    while not re.match('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',to_date):
        to_date = raw_input("Please indicate END DATE with format 'yyyy-mm-dd'(e.g. 2010-02-20): ")
       
    c.execute("select drugs.category, medications.drug_name, SUM(medications.amount) AS total_amount_prescribed from drugs, medications where medications.drug_name=drugs.drug_name and datetime(medications.mdate)>=datetime(:from_date) and datetime(medications.mdate)<=datetime(:to_date) GROUP BY drugs.category,medications.drug_name;",{"from_date":from_date, "to_date":to_date})

    result_list = c.fetchall()
    for i in range(len(result_list)):
        print(result_list[i])

    print('')
    print('')

#---------------------------------------------------------------  
def admin_query3():
    diagnosis=" "
    while diagnosis.isalpha() == False:
        diagnosis = raw_input("Enter diagnosis name: ")

    c.execute("select medications.drug_name as possible_medications from medications, diagnoses where diagnoses.diagnosis= :diagnosis and julianday(medications.mdate)>=julianday(diagnoses.ddate) group by medications.drug_name order by count(*) DESC;",{"diagnosis":diagnosis})
    
    result_list = c.fetchall()
    for i in range(len(result_list)):
        print(result_list[i])

    print('')
    print('')

#---------------------------------------------------------------        
def admin_query4():
    drug=" "
    while drug.isalpha() == False:
        drug = raw_input("Enter drug name: ")

    c.execute("select diagnoses.diagnosis as previous_diagnoses from diagnoses,medications where medications.drug_name=:drug and julianday(diagnoses.ddate)<julianday(medications.mdate) group by previous_diagnoses order by AVG(medications.amount);",{"drug":drug})

    result_list = c.fetchall()
    for i in range(len(result_list)):
        print(result_list[i])

    print('')
    print('')

    

#MAIN-----------------------------------------------------------





    
    
