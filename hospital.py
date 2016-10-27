from doctor import *


# commands:
DOC = ['search', 'add']
NURSE = []
ADMIN = []
# user[0] = role
# user[1] = staff id

# After user logs in, continuously ask what to do until they log out.

print "Available operations:",
if user[0] == "D":
     print ', '.join(DOC)
elif user[0] == "N":
    print ', '.join(NURSE)
else:
    print ', '.join(ADMIN)

while True:
    op = raw_input("Please enter an operation or 'logout' to quit: ").lower()
    #Doctors
    if user[0] == "D":
        if op == "search":
            get_chart()

        elif op == "add":
            line_type = raw_input("Enter line type ('S','D','M' or '0' to exit): ").upper()
            while line_type not in "SDM":
                line_type = raw_input("Enter line type ('S','D','M' or '0' to exit): ")
                if line_type == '0':
                    break
            if line_type == '0':
                continue

            add_line(line_type)

        elif op == 'logout':
            print "Goodbye!"
            break

        else:
            print "Invalid Command"

    # Nurse
    elif user[0] == "N":
        pass
        # Admin
    elif user[0] == "A":
        pass
