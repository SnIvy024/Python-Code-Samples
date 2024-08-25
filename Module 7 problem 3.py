# Your Name: Ivette Mujica
# The Date: 08/23/2024
# Problem 3 - This function to multiply all the numbers on the list. Use list [5, 2, 7, -1].

def multiply_list(numbers):
   
    result = 1 
    
     # Initializing result to 1
    
    # This loops through each number in the list and multiply it with the result.

    for number in numbers:
        result *= number
    
    return result  

# Example use
numbers = [5, 2, 7, -1]

  # The list of numbers to multiply
product = multiply_list(numbers)  

# it will calculate the product of the list
print(f"The product of the list {numbers} is {product}.")
