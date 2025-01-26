#a-z 
#0-9
#. _ time 1
# @ time 1
#. time 2,3
import re
def emailVerify(email):
    if re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@][a-z]+[.][a-z]{2,3}$', email):
        return True
    else:
        return False
email = input("Enter email: ")
if emailVerify(email):
    print("Email is valid")
else:
    print("Email is invalid")

# Output:
# Enter email:
# Email is valid
