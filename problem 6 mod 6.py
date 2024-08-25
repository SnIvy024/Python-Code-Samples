# Ivette Mujica
# 08/11/2024
# Problem 6 MOD 6: we find factorial using a for loop and compare it with math.factorial

import math

# Function to calculate factorial using a for loop

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Asking user for input

user_input = int(input("Enter a positive integer: "))

# Calculate factorial using the custom function

calculated_factorial = calculate_factorial(user_input)

# Calculate factorial using math.factorial

math_factorial = math.factorial(user_input)

#results
print(f"Calculated factorial (using custom function): {calculated_factorial}")
print(f"Calculated factorial (using math.factorial): {math_factorial}")
