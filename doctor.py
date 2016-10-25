from authentication import *
import datetime

# 1. For a given patient, list all charts in the system ordered by adate
# (indicating also whether they are closed or open). The user should be
# given the option to select a chart. Once a chart is selected, all entries
# (symptoms, diagnoses, and medications) associated with that chart must be
# listed, and the result must be ordered by the date of the entries.


def get_chart():
    patient = raw_input("Enter patient health care number or 0 to exit: ")

    while not patient.isdigit() and patient != '0':
        patient = raw_input("Enter patient health care number or 0 to exit: ")

    list_charts(patient)
    chart_num = raw_input("Enter chart id to view chart or '0' to exit: ")

    while not chart_num.isdigit():
        chart_num = raw_input("Enter chart id to view chart or '0' to exit: ")

    list_entries(chart_id)
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
    condition = "chart_id = '{0}' AND hcno = '{1}'".format(chart_id, patient)
    c.execute("SELECT * FROM (SELECT staff_id, symptom AS entry, obs_date AS date from symptoms WHERE :condition UNION SELECT staff_id,drug_name, mdate FROM medications WHERE :condition UNION SELECT staff_id, diagnosis, ddate FROM diagnoses WHERE :condition) ORDER BY date", {"condition":condition})
    return

# 2. For a given patient and an open chart of the patient add an entry for
# symptoms. The date obs_date should be set to the current date and time.

def add_symptom(patient, chart, ):
    # ('10000', '000','123', '2010-10-02','uncontrollable gas' )
    time = datetime.now().isoformat()
    line = patient chart user[3] time


    c.execute(INSERT INTO symptoms ())
    return

# 3. For a given patient and an open chart of the patient add an entry for
# diagnosis. The date ddate should be set to the current date and time.

# 4. For a given patient and an open chart of the patient add an entry for
# medications. The date mdate should be set to the current date and time.
# Additional checks should be performed before adding the entry: (1) if
# the prescribed amount for the patient is larger than the recommended
# amount sug_amount for that drug and the patient's age group, a warning
# should be issued that contains the information about recommended amount for
# a patient for that age group, and the doctor should be given the choice to
# confirm his prescription or to change the amount. (2) If the patient could be
# allergic to the prescribed drug drug_name, a warning should be issued that
# contains the information about the reported allergy; the warning should display
# the name of the drug that the patient reported being allergic to, and, if that
# is not directly drug_name, the name of the drug D  should be dsiplayed, which
# the patient reported being allergic to and from which it can be "inferred"
# that the patient may also be allergic to drug_name.
