# PROG 5.3 Handling Type Conversion

def add(x:int,y:int):
    """
    returns the sum of two numbers
    """
    return x+y
total_sum = int(input("Enter value of total sum :"))
bonus_points = int(input("Enter values of bonus points :"))
final_score = add(total_sum,bonus_points)

print(f"Data Type of total sum is {type(total_sum)} and \n " + f"bonus_points is {type(bonus_points)}")
print(f"Final score is {final_score}")
