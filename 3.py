# Write The Code Here
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

number = int(input("Enter the number to find the factorial : "))
result = factorial(number)
print(f"Factorial of {number} is {result}")