'''
Given a password, validate it. Password should have following attributes:
●length between 8 and 15 characters
●at least 1 capital, small letter
●at least 1 special symbol
●at least 1 number
●shouldn’t contain these words:”qwerty”, “asd” and it must be case insensitive.
'''
import re
print("Write your password: ")
password = input()

def validate_password(password):
    # ●length between 8 and 15 characters
    
    if not re.match(r'^.{8,15}$', password):
        return False

    '''
    ●at least 1 capital, small letter
    ●at least 1 special symbol
    ●at least 1 number
    '''

    if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()-_+=])[0-9a-zA-Z!@#$%^&*()-_+=]*$', password):
        return False

    # ●shouldn’t contain these words:”qwerty”, “asd” and it must be case insensitive.

    if re.search(r'(?i)qwerty|asd', password):
        return False

    return True

if validate_password(password):
    print("Password is valid")
else:
    print("password is not valid")
