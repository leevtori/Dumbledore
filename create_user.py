
conn = sqlite3.connect('hospital.db')
c = conn.cursor()

def create_user():
    #generate unique staff ID
    staff_id=''
    raw_input("Enter unique staff ID with 3 digits: ")
    while not staff_id.isdigit():
        staff_id = raw_input("Staff ID was taken, please enter another 3 digit ID: ")
        
    #make user pick D, N, or A
    role = raw_input("Choose a role: ")

    #make sure name is only letters or spaces
    name = "1"
    while all(x.isalpha() or x.isspace() for x in name) == False):
        name = raw_input("Enter your name: ")

    #make sure username is only numbers or letters
    username = raw_input("Choose a username: ")

    #hash password afterwards
    password = raw_input("Enter your password: ")
    
    c.execute("INSERT INTO staff VALUES(:staff_id, :role, :name, :username, :password);",{"staff_id":staff_id, "role":role,"name":name, "username":username, "password":password})
    c.execute("SELECT * FROM staff WHERE staff_id =:staff_id;", {"staff_id":staff_id})
    conn.commit()
