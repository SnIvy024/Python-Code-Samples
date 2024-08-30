# Your Name: Ivette M
# The Date: 08/29/2024
# Problem 3: adding together all numbers until the Total is Greater Than 100
# Description: ask the user to enter numbers and keeps a running total of them. It continues to ask for numbers until the total of all entered numbers passes 100.

# start an empty list to store the numbers name of list is numbers

numbers = []

# total the sum to 0
total_sum = 0

# Start the while loop

while total_sum <= 100:

    #The user to enters a number

    user_input = int(input("Enter a number: "))
    
    #enter number to the list

    numbers.append(user_input)
    
    # Add the entered number to the current total

    total_sum += user_input

# Print the final list of numbers and the sum

print("List of entered numbers:", numbers)
print("Total sum:", total_sum)
