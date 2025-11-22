#Write a program that finds the largest of three numbers using only nested if statements, then simplify it using and and or logical operators.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
num3 = float(input("Enter third number: "))
# Using nested if statements
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3  
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
print(f"The largest number using nested if statements is: {largest}")
# Using logical operators
if (num1 >= num2) and (num1 >= num3):
    largest = num1  
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(f"The largest number using logical operators is: {largest}")
