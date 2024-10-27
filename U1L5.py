# Importig math library to call upon functions
import math

# Informing the user what the program will do
print("Area of a Norman Window Shape")

# defining variable radius as users input for circles radius
radius = input("Input the cirlcles radius: ")

# Coverting variable radius as float number
radius = float(radius)

# Formula to calculate the semicircle portion of total area
scircle = 0.5*math.pi*math.pow(radius, 2) 

# Area of a square since the sidelength is the diameter of the circle; 
# radius*2 is the sidelength of square
square = 4*math.pow(radius, 2)

# Adding the two areas for total Norman Window shape area
area = scircle + square

# Printing the area as a float
print("The area is:", area)
