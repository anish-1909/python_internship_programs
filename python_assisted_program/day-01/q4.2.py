# PROG 4.1 Proper Function Usage
def add(x:int,y:int):
    """
    returns the sum of two numbers
    """
    return x+y
total_sum = 10
bonus_points = 20
final_score = add(total_sum,bonus_points)

print(f"Data Type of total sum is {type(total_sum)} and \n " + f"bonus_points is {type(bonus_points)}")
print(f"Final score is {final_score}")
