# Your Name: Ivette Mujica
# The Date: 08/23/2024
# Problem 2 - This python function is to check whether a number is in a given range. Using range(1,10).

def check_in_range(num):
  
    # Checking if the number is in the range from 1 to 9

    if num in range(1, 10):
        print(f"{num} is in the range 1 to 9.")
    else:
        print(f"{num} is not in the range 1 to 9.")

# Example function calls

check_in_range(5)  # This prints that 5 is in the range.
check_in_range(10) # This prints that 10 is not in the range.
