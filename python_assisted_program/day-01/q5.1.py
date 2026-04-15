# PROG 5.1: Hard Coding Values
PI = 22/7
def calculate_area(radius):
    return PI* radius ** 2
radius = 2
total = calculate_area(radius)
print(f"Area of a Circle with radius = {radius} is  {total}")