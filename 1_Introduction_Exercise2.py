#Write a program that takes your name as input and prints a 
# personalized greeting along with a calculation of your birth year.
#input
name = input("Enter your name: ")
print("Hello, " + name + "!")
age = int(input("Enter your age: "))   
current_year = 2025 
birth_year = current_year - age
print("You were born in the year " + str(birth_year) + ".") 