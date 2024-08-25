# Your Name: Ivette Mujica
# The Date: 08/24/2024
# Problem 4 - this function that checks if a year is a leap year True if it is a leap year and False if not.

def is_leap_year(year):
   
    # Check if the year is evenly divisible by 4

    if year % 4 == 0:
        
        # If the year is divisible by 100, check if it is also divisible by 400

        if year % 100 == 0:
            if year % 400 == 0:
                return True  
            # Leap year
            else:
                return False  
            # Not a leap year
        else:
            return True 
            # Leap year
    else:
        return False 
            # Not a leap year

# Try the function with different years

print(is_leap_year(2020))  
#True
print(is_leap_year(1900))  
#False
print(is_leap_year(2000))  
#True
print(is_leap_year(2023))  
#False
