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

