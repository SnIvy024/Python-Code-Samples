# Your Name: Ivette Mujica
# The Date: 08/23/2024
# Problem 1 - Write a function areaOfCircle(r) which returns the area of a circle of radius r.

import math 

 # Importing the module to access the value of pi and other math functions

def areaOfCircle(r):
    """
    This function calculates the area of a circle given its radius.

    Parameters:
    r (float or int): The radius of the circle.

    Returns:
    float: The area of the circle.
    """

    area = math.pi * (r ** 2)
    return area

# Example function

radius = 5
circle_area = areaOfCircle(radius)  

# This will calculate the area for a circle with radius 5

print(f"The area of a circle with radius {radius} is {circle_area:.2f}.")
