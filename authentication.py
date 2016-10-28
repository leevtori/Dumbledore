# logs user in.
import hashlib
import re
import getpass
import sqlite3

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

    username = username.lower()

    password = getpass.getpass("Please enter your password: ")

    password = hashlib.sha224(password).hexdigest()
    c.execute("SELECT password, name, role FROM staff WHERE login = :username ;", {"username":username})
    info = c.fetchone()

    if not info or info[0] != password:
        print "Incorrect login or password"
        return
    else:
        print "Welcome, " + info[1]

    return (info[1], info[2])

#user = None
#while not user:
#    user = authenticate()
