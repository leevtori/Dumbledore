# logs user in.
import hashlib
import re
import getpass
import sqlite3
from create_user import *

# This function prompts the user for a login and password. It assumes that
# the username can only contain letters a-z, numbers 0-9 and underscores.
# If hashed password matches stored hash, and username, then return the name
# of the staff member and role. Else, return nothing. will loop until something
# is returned.

#Database connectiom
conn =	sqlite3.connect('hospital.db')
c =	conn.cursor()

def authenticate():
    username = raw_input("Please enter your username: ")

    if not re.match('^[a-zA-Z0-9_]+$', username):
        print ("Error: Invalid username.")
        return

    password = getpass.getpass("Please enter your password: ")

    password = hashlib.sha224(password).hexdigest()
    c.execute("SELECT password, role, name , staff_id FROM staff WHERE login LIKE :username ;", {"username":username})
    info = c.fetchone()

    if not info or info[0] != password:
        print "Incorrect login or password"
        return
    else:
        print "Welcome, " + info[2]
        # commands:
        DOC = ['search', 'add']
        NURSE = ['close_chart', 'create_chart', 'list_all', 'add_symptom']
        ADMIN = ['doctor_sum','drug_sum','pos_med','pos_diag']
        
        # After user logs in, continuously ask what to do until they log out.
        if info[1] == "D":
            print "you are a doctor"
            print "Available operations: ",
            print ', '.join(DOC)
        elif info[1] == "N":
            print "You are a nurse"
            print "Available operations: ",
            print ', '.join(NURSE)
        else:
            print "You are an admin"
            print "Available operations: ",
            print ', '.join(ADMIN)


    return (info[1], info[3])

def new_user():
    create_user()



# user log in
#user = None
#while not user:
#    user = authenticate()
