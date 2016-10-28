
import sqlite3
import re

conn = sqlite3.connect("hospital.db")
c = conn.cursor()
#---------------------------------------------------------------  
def admin_query1():
    print("List for each doctor the name and the total amount of each drug that the doctor prescribed in a specified period of time.\n")
    
    #prompt user to enter start and end date
    from_date = "" 
    #regular expression from http://www.regular-expressions.info/dates.html
    while not re.match('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',from_date):
        from_date = raw_input("Please indicate START DATE with format 'yyyy-mm-dd' (e.g. 2010-01-31): ")
        
    to_date = ""
    while not re.match('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',to_date):
        to_date = raw_input("Please indicate END DATE with format 'yyyy-mm-dd'(e.g. 2010-02-20): ")
    
    #execute task   
    c.execute("select staff.name, medications.drug_name,SUM(medications.amount) AS total_amount_prescribed from staff, medications where datetime(medications.mdate)>=datetime(:from_date) and datetime(medications.mdate)<=datetime(:to_date) and medications.staff_id=staff.staff_id GROUP BY medications.drug_name;",{"from_date":from_date, "to_date":to_date})

    #print results
    result_list = c.fetchall()
    print "Doctor  |Drug  |Total Amount"
    print "--------------------------------"

    if (len(result_list) == 0):
        print "None to display"

    for i in range(len(result_list)):
        s = []
        for j in range(len(result_list[i])):
            s.append(str(result_list[i][j]))
        print '| '.join(s)

    print('')
    print('')

#---------------------------------------------------------------  
def admin_query2():
    
    print("For each category of drugs, list the total amount prescribed for each drug in that category in a specified period of time.\n")

    #prompt user to enter date
    from_date = "" 
    #regular expression from http://www.regular-expressions.info/dates.html
    while not re.match('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',from_date):
        from_date = raw_input("Please indicate START DATE with format 'yyyy-mm-dd' (e.g. 2010-01-31): ")
       
    to_date = ""
    while not re.match('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',to_date):
        to_date = raw_input("Please indicate END DATE with format 'yyyy-mm-dd'(e.g. 2010-02-20): ")
       
    #execute task
    c.execute("select drugs.category, medications.drug_name, SUM(medications.amount) AS total_amount_prescribed from drugs, medications where medications.drug_name=drugs.drug_name and datetime(medications.mdate)>=datetime(:from_date) and datetime(medications.mdate)<=datetime(:to_date) GROUP BY drugs.category,medications.drug_name;",{"from_date":from_date, "to_date":to_date})

    #print results
    result_list = c.fetchall()
    print "Category  |Drug  |Total Amount"
    print "--------------------------------"

    if (len(result_list) == 0):
        print "None to display"

    for i in range(len(result_list)):
        s = []
        for j in range(len(result_list[i])):
            s.append(str(result_list[i][j]))
        print '| '.join(s)

    print('')
    print('')

#---------------------------------------------------------------  
def admin_query3():

    print("List for a given diagnosis all possible medications that have been prescribed over time after that diagnosis.\n")
    
    #prompt user to enter diagnosis name
    diagnosis = "1"
    while all(x.isalpha() or x.isspace() for x in diagnosis) == False:
        diagnosis = raw_input("Enter diagnosis name: ")

    diagnosis = diagnosis.lower()
    
    #execute task
    c.execute("select medications.drug_name as possible_medications from medications, diagnoses where lower(diagnoses.diagnosis)= :diagnosis and julianday(medications.mdate)>=julianday(diagnoses.ddate) group by medications.drug_name order by count(*) DESC;",{"diagnosis":diagnosis})
    
    #print results
    result_list = c.fetchall()
    print "Possible Medications"
    print "--------------------------------"

    if (len(result_list) == 0):
        print "None to display"

    for i in range(len(result_list)):
        s = []
        for j in range(len(result_list[i])):
            s.append(str(result_list[i][j]))
        print '| '.join(s)
    print('')
    print('')

#---------------------------------------------------------------        
def admin_query4():
    print("List for a given drug all the diagnoses that have been made before prescribing the drug.\n")

    #prompt user to enter drug name
    drug = "1"
    while all(x.isalpha() or x.isspace() for x in drug) == False:
        drug = raw_input("Enter drug name: ")
    drug = drug.lower()

    #execute task
    c.execute("select diagnoses.diagnosis as previous_diagnoses from diagnoses,medications where lower(medications.drug_name)=:drug and julianday(diagnoses.ddate)<julianday(medications.mdate) group by previous_diagnoses order by AVG(medications.amount);",{"drug":drug})

    #print results
    result_list = c.fetchall()
    print "Previous Diagnoses"
    print "--------------------------------"
    if (len(result_list) == 0):
        print "None to display"
    for i in range(len(result_list)):
        s = []
        for j in range(len(result_list[i])):
            s.append(str(result_list[i][j]))
        print '| '.join(s)

    print('')
    print('')

    


    
    
