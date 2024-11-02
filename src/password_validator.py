# password_validator.py
import re

def validate_passwords(input_passwords):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$'
    passwords = input_passwords.split(',')
    valid_passwords = [pwd for pwd in passwords if re.match(pattern, pwd)]
    return ','.join(valid_passwords)

