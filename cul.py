from IVT import *
from Polynomial import *

"""
Author : Adam Saad
   Revison date : January 22nd 2025
   Program : ICS4U0-1
   Description : A code that finds the roots of a given function
   
 General Variable Dictionary:
 - function (list[str]) the coefficients of the function
 - arr (list[str]) the filtered out version of the coefficients of the function
 - temp (list[str]) a list of coefficients each as their own term
 - func (list[int/float]) the final version of our list of coefficients as a float/int
 - x1 - (float) the first point the roots of the function can be found within
 - x1 - (float) the second point the roots of the function can be found within
"""


func = []
# These are the functions I used [1, -21, 175, -735, 1624, -1764, 720, 0] or [1,-10,35,-50,24]
#function = input("Please input the coefficients of a function as so... 3, 4, -2, 6 etc: ")
# an input option has been made in case you want to easily put in your own coefficients just comment out the bit of code below
function = (1,-10,35,-50,24)
function = str(function) # input a string for the coefficients of the function

arr = function.strip("()[]{}+") # get rid of uneccesary terms which may have been used
temp = arr.split(',') # split up input

for c in temp: 
    try:
        func.append(float(c)) # try making the coefficients into floats
    except ValueError:
        print("Please input a set of numbers with commas in between") # if a value error occurs output the issue to let the user know and exit the code
        exit()

Poly = Polynomial(func) 
Poly.craft() 
print("f(x) = ", Poly) # print the function

x1 = input("Please input the first point your root can be found between: ") # take input on the range the roots can be found within
x2 = input("Please input the second point your root can be found between: ")
try:
    x1 = float(x1) # make these values into floats
    x2 = float(x2)
except ValueError:
    print("please input a proper number for your points") # if a value error occurs output the issue to let the user know and exit the code
    exit()

Zero = IVT(func)
print(Zero.findZero(x1, x2)) # find zeros.
