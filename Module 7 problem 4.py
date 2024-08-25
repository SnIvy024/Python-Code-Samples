# Your Name: Ivette Mujica
# The Date: 08/23/2024
# Problem 4 - This function takes a list of numbers and returns a new list with unique elements of the first list. Using
# the list from the docs [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.

def unique_elements(numbers):
    
    unique_list = []
    #start an empty list to store unique elements.
    
    #Loop them through each number in the input list.

    for number in numbers:

        # If the number is not already in the unique_list i add it

        if number not in unique_list:
            unique_list.append(number)
    
    return unique_list 

 # Return the list containing unique elements.


numbers = [1, 3, 3, 3, 6, 2, 3, 5]  
#list with duplicate elements
unique_list = unique_elements(numbers) 
#Get the list with unique elements
print(f"The list with unique elements is {unique_list}.")
