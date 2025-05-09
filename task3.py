import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
email_input = input("Enter an email address: ")
if is_valid_email(email_input):
    print("The email is valid.")
else:
    print("The email is invalid.")
