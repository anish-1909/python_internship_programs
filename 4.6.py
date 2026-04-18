name="john"
age = 25
height= 5.845
simple_formatted = f"Name : {name} , Age : {age} , Height : {height}"
print(f"Simple formatted String: \n {simple_formatted}\n\n")
expression_formatted = f"Name:{name.upper()} , Age : {age + 5} . Height : {round(height,2)} feet"
print(f"Formatted string with Expressions: \n {expression_formatted},end=\n\n")

person ={"name":name,"age":age,"height":height}
dict_formatted = f"Name: {person["name"]}, Age:{person["age"]} , height:{person["height"]}feet tall"
print(f"Formatted string with multiline text: \n {dict_formatted},end =\n\n")
print(f"""Person Details:
        Name:{person["name"]},
        Age:{person["age"]},
        Height:{person["height"]:.02f} feet""")