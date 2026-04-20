import re

def input_string(s):
    new_string = re.findall('\d{1}',s)
    return new_string
    

string = input("Enter a String : ")
output = input_string(string)
if output:
    print(f"digits found in the string : {output}")
else:
    print("No digits found")