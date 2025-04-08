# Problem 1
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Name:", name)
print("Age:", age)
print("Type of name:", type(name))
print("Type of age:", type(age))

# Problem 2
num1 = input("first number: ")
num2 = input("second number: ")

num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print("The first number is larger.")
elif num2 > num1:
    print("The second number is larger.")
else:
    print("Both numbers are equal.")
# Problem 3
favorite_color = input("What is your favorite color? ")

color_type = type(favorite_color)

print("Your favorite color is:", favorite_color)
print("The type of this value is:", color_type)
# Problem 4
user_input = input("Enter a floating-point number: ")

float_number = float(user_input)

print("You entered:", float_number)
print("The type of this value is:", type(float_number))

# Problem 5
full_name = input("Enter your full name: ")

name_length = len(full_name)

print("The length of your name is:", name_length)
print("The type of this value is:", type(name_length))