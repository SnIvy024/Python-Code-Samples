# Your name: Ivette Mujica
# Date: 07/21/2024

# Problem 1: Write a program that prints "Hello World" to the screen.

def problem1():
    # This prints "Hello World" to the screen.
    print("Hello World")

# Then Test Problem 1
problem1()


# Problem 2: Write a program that asks the user for their name and greets them with their name.

def problem2():
    # This function asks for the user's name and greets them.
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

# Then Test Problem 2
# problem2()


# Problem 3: Modify the previous program such that only the users you and your instructor are greeted with their names.

def problem3():
    # This function asks for the user's name and greets only specific users like teachers.
    name = input("Enter your name: ")
    if name == "Ivette" or name == "Professor name":
        print(f"Hello, {name}!")
    else:
        print("Hello, user!")

# Then Test Problem 3
# problem3()


# Problem 4: Write a program that will compute the area of a circle. 
# Prompt the user to enter the radius and print a nice message back to the user with the answer.

def problem4():
    # This function outputs the area of a circle given the radius.
    import math
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle with radius {radius} is {area:.2f}")

# Then Test Problem 4
# problem4()


# Problem 5: Write a program that will compute MPG for a car. 

# Prompt the user to enter the number of miles driven and the number of gallons used. 

# Print a nice message with the answer.

def problem5():
    # This function computes the miles per gallon (MPG) for a car.
    miles = float(input("Enter the number of miles driven: "))
    gallons = float(input("Enter the number of gallons used: "))
    mpg = miles / gallons
    print(f"The car's MPG is {mpg:.2f}")

# Then Test Problem 5
# problem5()


# Problem 6: Write a program that will convert degrees Fahrenheit to degrees Celsius.

def problem6():
    # This function converts Fahrenheit to Celsius.
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"The temperature in Celsius is {celsius:.2f}")

# then Test Problem 6
# problem6()


# Problem 7: It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. 
# If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights 
# you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting 
# day number, and the length of your stay, and it will tell you the number of day of the week you will return on.

def problem7():
    # This function calculates the return day after a given number of days away.
    start_day = int(input("Enter the starting day number (0 for Sunday, 6 for Saturday): "))
    stay_length = int(input("Enter the length of your stay (in nights): "))
    return_day = (start_day + stay_length) % 7
    print(f"You will return on day number {return_day}")

# then Test Problem 7
# problem7()

 
