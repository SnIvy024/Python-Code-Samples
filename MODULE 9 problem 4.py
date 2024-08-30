# Your Name: Ivette M
# The Date: 08/29/2024
# Problem 4:adding Multiples of 10 to a List
# # Description: use a while loop to add values divisible by 10 to a list called 10' loop runs until the counter reaches 50.

# start the counter variable

counter = 0

# Start an empty list to keep the multiples of 10

tens = []

# Start the while loop

while counter <= 50:
    # Checking if the counter is divisible by 10

    if counter % 10 == 0:
        # add the counter value to the list

        tens.append(counter)
    
    # add the counter by 1

    counter += 1

# Print the list for the results

print("List of numbers divisible by 10:", tens)
