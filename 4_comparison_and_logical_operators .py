#Use comparison and logical operators (and, or, not) to check if 
# a user's age is between 18 and 65, inclusive, but not exactly 30.

age = int(input("Enter your age: "))
is_eligible = (age >= 18 and age <= 65) and (age != 30)
if is_eligible:
    print("You are eligible.")  
else:
    print("You are not eligible.")  