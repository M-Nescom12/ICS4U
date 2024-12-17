import math
import turtle

class point:
    def __init__(self, x: float=None, y: float=None):
        # PreConditions and Purpose: Initialize a Point object with x and y coordinates.
        # x, y can be floats or None for the creation of a head node in a circular linked list.
        # PostConditions: Creates a Point object with default x, y as None and next as None.
        
        self.__x = x  # x-coordinate of the point (type: float or None)
        self.__y = y  # y-coordinate of the point (type: float or None)
        self.next = None  # Pointer to the next point in the circular linked list (type: Point or None)

    def valid(self):
        # PreConditions and Purpose: Validate the x and y coordinates to ensure they are numbers.
        # PostConditions: Converts x and y to int or float (tries before int before float), or exits if invalid.

        try:
            self.__x = int(self.__x)
            self.__y = int(self.__y)
        except ValueError:
            try:
                self.__x = float(self.__x)
                self.__y = float(self.__y)
            except ValueError:
                print("x and y coordinates must be numbers")
                exit()

    def get_coordinates(self):
        # PreConditions and Purpose: Retrieve the x and y coordinates of the Point.
        # PostConditions: Returns a tuple (x, y) as floats.
        return float(self.__x), float(self.__y)

    def __str__(self):
        # PreConditions and Purpose: Represent the Point object as a string in the format "(x, y)".
        # PostConditions: Returns a string representation of the Point.

        return f"({self.__x}, {self.__y})"
    
class Polygon:
    def __init__(self):
    # PreConditions and Purpose: Initialize a Polygon object.
    # PostConditions: Creates a Polygon with default values and an empty circular linked list of points.
        self.__sides = 0  # Number of sides in the polygon (type: int)
        self.__vertices = 0  # Number of vertices in the polygon (type: int)
        self.__head = None  # Head node of the circular linked list (type: Point or None)
        self.__head_angle = 0


    def add_point(self, x: float, y: float):
        # PreConditions: Add a new point (x, y) to the polygon as part of a circular linked list.
        # PostConditions: Adds a new Point to the circular linked list and updates vertex count.

        # Variable dictionary:
        # - V (Point): The new point to be added.
        # - h (Point): Traversal pointer to find the last point in the circular linked list.

        V = point(x, y)
        if self.__head is None:
            # First point: Initialize head and make it circular.
            self.__head = V
            V.next = V
        else:
            # Add the new point to the circular linked list.
            h = self.__head
            while h.next != self.__head:
                h = h.next
            h.next = V
            V.next = self.__head
        self.__vertices = self.__vertices + 1
        if self.__vertices > 1:
            self.__sides = self.__vertices
    
    def point_dist(self):
        side_lens = []
        side = self.__head
        [x1, y1] = side.get_coordinates()
        [x2, y2] = side.next.get_coordinates()
        dist = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
        side_lens.append(dist)
        side = side.next
        while side != self.__head:
            [x1, y1] = side.get_coordinates()
            [x2, y2] = side.next.get_coordinates()
            dist = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
            side_lens.append(dist)
            side = side.next
        return side_lens
    
    def internal_angle(self):
        angles = []
        vert = self.__head
        [x1, y1] = vert.get_coordinates()
        [x2, y2] = vert.next.get_coordinates()
        [x3, y3] = vert.next.next.get_coordinates()
        dotV = float((x1-x2)*(x3-x2)) + ((y1-y2)*(y3-y2))
        
        mag_sum = abs(math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2)))*(math.sqrt(((x3 - x2)**2) + ((y3 - y2)**2)))
        if mag_sum != 0:
            theta2 = (math.acos((dotV/mag_sum)))*(180/math.pi)
            vert = vert.next
        else:
            print("No duplicate points...")
            exit()
        while vert != self.__head:
            if vert.next == self.__head:
                [x2, y2] = vert.next.get_coordinates()
                [x3, y3] = vert.next.next.get_coordinates()
                dotV = float(( (x2-1) - x2)*(x3 - x2)) + ((y2-y2)*(y3-y2))
                
                mag_sum = abs(math.sqrt((( (x2-1) - x2)**2) + ((y2 - y2)**2)))*(math.sqrt(((x3 - x2)**2) + ((y3 - y2)**2)))
                if mag_sum != 0:
                    self.__head_angle = (math.acos((dotV/mag_sum)))*(180/math.pi)
                    if self.__head_angle > 90:
                        self.__head_angle = self.__head_angle - 90
                else:
                    self.__head_angle = 0
            if vert == self.__head.next.next:
                angles.append(theta2)
            [x1, y1] = vert.get_coordinates()
            [x2, y2] = vert.next.get_coordinates()
            [x3, y3] = vert.next.next.get_coordinates()
            dotV = float((x1-x2)*(x3-x2)) + ((y1-y2)*(y3-y2))  
            mag_sum = abs(math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2)))*(math.sqrt(((x3 - x2)**2) + ((y3 - y2)**2)))
            if mag_sum != 0:
                theta = (math.acos((dotV/mag_sum)))*(180/math.pi)
                angles.append(theta)
                vert = vert.next
            else:
                print("No duplicate points...")
                exit()
        return angles
        
    def draw_polygon(self):
        turtle.speed(1)  
        turtle.penup()
        lengths = self.point_dist()
        angles = self.internal_angle()
        V = self.__head
        if self.__head_angle != 0 and self.__head_angle != 180 and self.__head_angle != 90 and self.__head_angle != 270:
            for i in range(self.__sides):
                if i == 0:
                    [x, y] = V.get_coordinates()
                    turtle.setpos(x, y)
                    turtle.pendown()       
                    turtle.left(self.__head_angle)
                    turtle.forward(lengths[i])
                else:
                    if angles[i] > 90:
                        turtle.left(angles[i]-90)
                        turtle.forward(lengths[i])
                        V = V.next
                    else:
                        turtle.left(angles[i])
                        turtle.forward(lengths[i])
                        V = V.next
        else:
            [x, y] = V.get_coordinates()
            turtle.setpos(x, y) 
            for i in range(self.__sides):
                turtle.pendown()       
                turtle.right(angles[i])
                turtle.forward(lengths[i])
                V = V.next
        turtle.done()
        
    def draw_Poly(self):
        turtle.shape("circle")
        turtle.shapesize(0.1,0.1)
        turtle.speed(1)
        turtle.penup()
        V = self.__head
        [x, y] = V.get_coordinates()
        turtle.setpos(x, y)
        turtle.pendown()
        V = V.next
        while  V != self.__head:
            [x0, y0] = V.get_coordinates()
            turtle.goto(x0, y0)
            V = V.next
        [x0, y0] = V.get_coordinates()
        turtle.goto(x0, y0)
        turtle.done()
        
    def __str__(self):
        # PreConditions: Generate a string representation of the polygon as a series of points.
        # PostConditions: Returns the circular linked list of points in the format "(x, y) -> (x, y) -> ...".
        if self.__vertices < 3: # Checking if there are enough points to be a polygon
            return "Not enough coordinates found"
        
        # Variable dictionary:
        # - nodes (list): List of point strings.
        # - V (Point): Traversal pointer to traverse the circular linked list.

        nodes = []
        V = self.__head 
        nodes.append(str(V))  # Appending the head point to nodes
        V = V.next # Moving to the next node from the head of the lsit
        while V != self.__head:
            nodes.append(str(V))
            V = V.next
        return " -> ".join(nodes) 
"""
Author : Muntasir Nathalia
   Revison date : December 7th 2024
   Program : ICS4U0
   Description : Takes input from a file containing a list of polygon vertexes/coordinates and returns information back
   
 General Variable Dictionary:
 - fh (file object): File handle for reading the input file
 - polydata (str): Raw data line from the file
 - cord (list): List of parsed points from the file
 - Poly (Polygon): The Polygon object from poly.py

"""

# Import code from poly.py
from poly import *

def getNumeric(data : str):
    # input: data is a point in the format "(x,y)" (type str)
    # output: A list indicating a point (x, y) where x, y are int or float
    
    arr = data.split(', ') # Spliting the points up
    PS = [] # Initializing list to store points as int or float
    for c in arr: 
        p = c.strip("()") # Stripping the brackets from the point
        [x,y] = p.split(',') # Splitting the x and y
        pt = point(x, y) # Declaring point object 
        pt.valid() # Converting the the coordinates to int or float
        PS.append([x,y]) # Appending to a list 
    return PS 

fh = open("a2.txt", "r") # this is the name of the data file to open
polydata = fh.readline().strip() # Stripping the data file
cord = getNumeric(polydata) # Passing polydata into function getNumeric to genrate x,y pair in int stored in a list
Poly = Polygon() # Declaring Polygon object
# Looping through all the points in the list and creating a linked list using (Poly.add_point)
for z in range(len(cord)):
    x = cord[z][0]
    y = cord[z][1]
    Poly.add_point(x,y)
    

print(Poly) # this should print the entire linked list of points as string
print(Poly.point_dist())
print(Poly.internal_angle())
Poly.draw_polygon()
#Poly.draw_Poly()

