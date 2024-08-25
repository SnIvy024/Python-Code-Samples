# Your Name: Ivette Mujica
# The Date: 08/24/2024
# I define a function that checks whether the value 5 from the numbers. If 5 is found, then print a message showing itself if not print a different message.

def check_for_five(input_list):
   
# Checking if 5 is in the list

    if 5 in input_list:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")

# Test the function with different lists

test_list1 = [1, 2, 3, 4, 5]
test_list2 = [10, 20, 30, 40]
test_list3 = [5, 5, 5, 5, 5]

check_for_five(test_list1) 
 #the value 5 is in the list.
check_for_five(test_list2) 
 #the value 5 is not in the list.
check_for_five(test_list3) 
 #the value 5 is in the list.
