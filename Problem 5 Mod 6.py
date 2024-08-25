# Ivette Mujica
# 08/11/2024
# Problem 4 Mod 6: Approximate Pi and compare it with math.pi

import math

# Method 1: Using the Leibniz formula for Pi (I looked this method up)
# Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - etc
# So Pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - etc

def approximate_pi(terms):
    pi_approximation = 0
    for i in range(terms):

        # The denominator is odd numbers

        denominator = 2 * i + 1

        # Alternating subtract if i is odd, add if i is even

        term = (-1) ** i / denominator
        pi_approximation += term
    return 4 * pi_approximation

# Choose the number of terms to include in the approximation

number_of_terms = 10000
approximated_pi = approximate_pi(number_of_terms)

# results

print(f"Approximated Pi (using {number_of_terms} terms): {approximated_pi}")
print(f"Value of math.pi: {math.pi}")
