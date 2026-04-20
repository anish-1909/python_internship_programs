import re
def is_valid(email):
    pattern = r'^[a-zA-Z0-9._+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    new_valid =re.match(pattern,email)
    return new_valid

email=input("Enter email address :")
v_mail=is_valid(email)
if v_mail:
    print(f"{email} is a valid email")
else:
    print(f"{email} is not a valid email")