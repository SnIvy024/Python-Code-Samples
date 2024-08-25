# Your Name: Ivette Mujica
# The Date: 08/23/2024
# Problem 6 - Importing a turtle and modify the turtle graphics code to make a series of nested squares

import turtle

def drawSquare(t, sz):

    for i in range(4): 
     # Draw a square with four sides
        t.forward(sz) 
     # Move the turtle forward by the size of the square
        t.left(90)     
     # Turn the turtle 90 degrees to the left

# This is to set up the screen and turtle

wn = turtle.Screen()      
alex = turtle.Turtle()    
alex.color("blue")        

# This Draws multiple squares

size = 20  
# start size of the square
for _ in range(10): 
 # Draw 10 squares
    drawSquare(alex, size)  
# Draw a square with the current size
    size += 20
# Increase the size for the next square
    alex.penup() 
# Lift the pen 
    alex.goto(-size / 2, -size / 2)  
# Move to the new starting point for the next square
    alex.pendown()  
# Lower the pen 

wn.exitonclick()
