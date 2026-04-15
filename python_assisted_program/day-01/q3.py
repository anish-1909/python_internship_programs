# PROG 3: Define Function

#BAD
#Cryptic variable names

x = 10
y = 20
z = x + y
print(f"The value z is {z}")

#GOOD

#Defining function block for add 

def add(x,y):
    return x+y
total_sum = 10
bonus_points = 20
final_score = add(total_sum,bonus_points)
print(f"Final score is {Final_score}")
