# Your Name: Ivette Mujica
# The Date: 08/24/2024
# Problem 2 - two inputs from the user, calculates their sum, and checks if the sum is greater than, less than, or equal to 10. It then print it all.

def check_sum():
  
    # Taking two inputs from the user and converting them to integers

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Calculating the sum

    total = num1 + num2
    
    # Checking if the sum is greater than, less than, or equal to 10

    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")


check_sum() 
 # the user will enter two numbers, then print if the sum is greater than, less than, or equal to 10.
