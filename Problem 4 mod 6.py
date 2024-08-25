# Ivette Mujica
# 08/11/2024
# Problem 5 Mod 6: Change radians to degrees and compare it with math.degrees

import math

# Use Function to convert radians to degrees

def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return degrees

# Ask the user for input in radians

radian_value = float(input("Enter the value in radians: "))

# Calculate degrees using the custom function

calculated_degrees = radians_to_degrees(radian_value)

# Calculate degrees using math.degrees

math_degrees = math.degrees(radian_value)

#results

print(f"Calculated degrees (using custom function): {calculated_degrees}")
print(f"Calculated degrees (using math.degrees): {math_degrees}")
