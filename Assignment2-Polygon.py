import math
class Point:
   def __init__(self, x, y):
      self.__x = x
      self.__y = y

   def distance(self, p2):
      return math.sqrt((self.__x-p2.x)**2 + (self.__y-p2.y)**2)
    
ups = input("Enter the coordinates of your polygon in order with the format: a b, x y, ...")
ups.cleanup()
#a2.txt = file
#driver.py = driver file
#class polygon in poly.py
#It should be instantiated to some object variable with the following call: myPoly = Polygon()
#points are added using myPoly.addPoint(x, y) until the past point is entered. 
#where myPoly is an instance of Polygon()
#myPoly creates an array of Point() objects
#A call to compute area (myPoly.area()) should return floating point.
#similarly, the perimeter (myPoly.perimeter()) should also return floating point.

triangle = Polygon()
triangle.add_point(1, 1)
triangle.add_point(1, 2)
triangle.add_point(2, 2)
