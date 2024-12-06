import math

class point:
    def __init__(self, x: float=None, y: float=None):
        # Default is None due to creation of a Head Node for linked lists
        self.__x = x
        self.__y = y
        self.next = None

    def valid(self):
        # A validator is needed mostly for when we go to the end of the file, but
        # also to assure us that the point is properly formatted with either
        # ints or floats.

        try:
            self.__x = int(self.__x)
            self.__y = int(self.__y)
        except ValueError:
            self.__x = float(self.__x)
            self.__y = float(self.__y)
    
    def __str__(self):
        # point (x, y) expressed this way as string
        # as in: (4, 5)
        return f"({self.__x}, {self.__y})"
    
class Polygon:
    def __init__(self):
        # Set basic properties to default values
        self.__sides = 0
        self.__vertices = 0
        self.__head = None # a null point with a null Next field

    def add_point(self, x: float, y: float):
        # initialize a point object V
        # if it is the first point, create the object with variable V make head.next point to V
        # if it is any other point, V.next points to it, and V traverses to that point
        # count the vertices as you go
        V = point(x, y)
        if self.__head is None:
            self.__head = V
            V.next = V
        else:
            J = self.__head.next
            while J.next != self.__head:
                J = J.next
            J.next = V
            V.next = self.__head
        self.__vertices = self.__vertices + 1
       
    
    def __str__(self):
        # Use a traversal to generate the entire set of points separated by "->" as string
        # You need to use point's __str__ function to help you.
        if self.__head is None:
            return "Empty Polygon"
        result = []
        J = self.__head
        while True:
            result.append(str(J))
            J = J.next
            if J == self.__head:
                break
        return " -> ".join(result)
    

def getNumeric(data : str):
    # input: S is a point in the format "(x,y)" (type str)
    # output: a tuple or list indicating a point (x, y) where x, y are int or float
    arr = data.split(', ')
    Point = []
    for c in arr:
        p = c.strip("()")
        [x,y] = p.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            x = float(x)
            y = float(y)
        Point.append([x,y])
    return Point
            

fh = open("a2.txt", "r") # this is the name of the data file to open
polydata = fh.readline().strip()
Points = getNumeric(polydata)
Poly = Polygon()
for z in range(len(Points)):
    x = Points[z][0]
    y = Points[z][1]
    Poly.add_point(x,y)
# declare a polygon
# loop through the points array and turn them into numbers for the polynomial object
    # generate an x, y pair (numerical not str) from getNumeric
    # add to the polynomial (call add_point())

#print(Poly) # this should print the entire linked list of points as string
        


