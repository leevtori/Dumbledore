from authentication import *

# 1. For a given patient, list all charts in the system ordered by adate
# (indicating also whether they are closed or open). The user should be
# given the option to select a chart. Once a chart is selected, all entries
# (symptoms, diagnoses, and medications) associated with that chart must be
# listed, and the result must be ordered by the date of the entries.



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


# 2. For a given patient and an open chart of the patient add an entry for
# symptoms. The date obs_date should be set to the current date and time.
# 3. For a given patient and an open chart of the patient add an entry for
# diagnosis. The date ddate should be set to the current date and time.

<<<<<<< HEAD
# add_line function is used for 2 and 3 and calls another function for 4
=======
def add_symptom(patient, chart, ):
    # ('10000', '000','123', '2010-10-02','uncontrollable gas' )
   # time = datetime.now().isoformat()
   # line = patient chart user[3] time
>>>>>>> 25fdc5ace2511a86465b77890fdd10650c6fda0d

def add_line(Ctype):
    patient = raw_input("Enter patient HCN: ")
    chart = raw_input("Enter chart ID: ")

<<<<<<< HEAD
    c.execute("SELECT chart_id FROM charts WHERE edate IS NULL AND chart_id = :chart AND hcno = :patient ;",{"chart":chart, "patient":patient})
    if not c.fetchone():
        print "Chart does not exist or is not open."
        return
    if Ctype != "M":
        content = raw_input("Enter the content of the chart: ")
=======
    #c.execute(INSERT INTO symptoms ())
    return
>>>>>>> 25fdc5ace2511a86465b77890fdd10650c6fda0d

    if Ctype == "S":
        c.execute("INSERT INTO symptoms VALUES ('{0}', '{1}' , '{2}' , datetime('now') , '{3}' ) ;".format (patient, chart, user[1], content) )
    elif Ctype == "D":
        c.execute("INSERT INTO diagnoses VALUES ('{0}', '{1}' , '{2}' , datetime('now') , '{3}' );".format (patient, chart, user[1], content))
    else:
        add_med(patient, chart)
    conn.commit()

# 4. For a given patient and an open chart of the patient add an entry for
# medications. The date mdate should be set to the current date and time.
# Additional checks should be performed before adding the entry:

# (1) if the prescribed amount for the patient is larger than the recommended
# amount sug_amount for that drug and the patient's age group, a warning
# should be issued that contains the information about recommended amount for
# a patient for that age group, and the doctor should be given the choice to
# confirm his prescription or to change the amount.

# (2) If the patient could be allergic to the prescribed drug drug_name, a
# warning should be issued that contains the information about the reported
# allergy; the warning should display the name of the drug that the patient
# reported being allergic to, and, if that is not directly drug_name, the name
# of the drug D  should be dsiplayed, which the patient reported being allergic
# to and from which it can be "inferred"that the patient may also be allergic
# to drug_name.

def add_med(patient, chart):
    drug_name = raw_input("Enter drug name or '0' to exit: ")
    if drug_name == '0': return
    # Check that drug exists.
    c.execute("SELECT * FROM drugs WHERE drug_name LIKE :drug_name;", {"drug_name":drug_name})
    # if drug does not exist, promt user for another one.
    test = c.fetchone()
    while not test:
        print("Invalid name")
        drug_name = raw_input("Enter drug name: ")
        if drug_name == '0': return
        c.execute("SELECT * FROM drugs WHERE drug_name LIKE :drug_name;", {"drug_name":drug_name})
        test = c.fetchone()
# check allergy
    allergic = False
    c.execute("SELECT * FROM reportedallergies WHERE drug_name LIKE :drug_name AND hcno = :patient ;", {"drug_name":drug_name, "patient":patient})
    rep_allerg = c.fetchone()
    if rep_allerg:
        print "Warning: Patient has repoted allergy to " + drug_name
        allergic = True

    c.execute("SELECT alg FROM inferredallergies, reportedallergies WHERE alg LIKE drug_name AND canbe_alg LIKE :drug_name AND hcno = :patient ;", {"drug_name":drug_name, "patient":patient})
    inf_alg = c.fetchall()
    for alg in inf_alg:
        allergic = True
        print "Warning: patient has reported an allergy to " + alg[0] + ". It can be inferred that patient is allergic to " + drug_name

    if allergic:
        cont = raw_input ("Continue adding drug (Y/N)? ")

        if cont.lower() == "n":
            return

# get amount
    amount = raw_input("Enter amount in mg (ex. 10): ")
    # if amount is not a number
    if not amount.isdigit():
        amount = raw_input("Invalid entry. Enter amount in mg (ex. 10): ")
    c.execute("SELECT d.sug_amount FROM patients p, dosage d WHERE d.drug_name LIKE :drug_name AND d.age_group == p.age_group AND p.hcno = :patient ;", {"drug_name":drug_name, "patient":patient})
    sug_amount = c.fetchone()[0]

# check suggested amount
    if int(amount) > sug_amount:
        change = raw_input("Prescription amount greater than recommended for age group. Would you like to change your amount to the recommended amount? (Y/N) ").lower()
        if change == 'y':
            amount = sug_amount
# get start and end dates
    start = raw_input("Enter start date (YYYY-MM-DD): ")
    while not re.match('((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])', start):
        start = raw_input("Invalid date. Enter start date (YYYY-MM-DD): ")
    end = raw_input("Enter end date (YYYY-MM-DD): ")
    while not re.match('((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])', end):
        end = raw_input("Invalid date. Enter end date (YYYY-MM-DD): ")

    c.execute("INSERT INTO medications VALUES ('{0}' , '{1}' , '{2}', datetime('now') , '{3}' , '{4}' , '{5}' , '{6}') ;".format(patient, chart, user[1] , start, end , amount , drug_name))
