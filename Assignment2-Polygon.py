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
        except:
            self.__
            return val

    def __str__(self):
        # point (x, y) expressed this way as string
        # as in: (4, 5)
        pass

class Polygon:
    def __init__(self):
        # Set basic properties to default values
        self.__sides = 0
        self.__vertices = 0
        self.__head = point() # a null point with a null Next field

    def add_point(self, x: float, y: float):
        # initialize a point object V
        # if it is the first point, create the object with variable V make head.next point to V
        # if it is any other point, V.next points to it, and V traverses to that point
        # count the vertices as you go
        new_point = Node(data)
        if tail is None:
            tail = new_point
            new_point.next = new_point
        else:
            new_point.next = tail.next
            tail.next = new_point
            tail = new_point
        return tail
        pass

    def __str__(self):
        # Use a traversal to generate the entire set of points separated by "->" as string
        # You need to use point's __str__ function to help you.
        pass
        








def getNumeric(S : str):
    # input: S is a point in the format "(x,y)" (type str)
    # output: a tuple or list indicating a point (x, y) where x, y are int or float
    x = None
    y = None # obiviously, change these

    return (x, y)

fh = open("a2.txt", "r") # this is the name of the data file to open

polydata = fh.readline().strip()
arr = polydata.split(', ')
for c in arr:
    p = c.strip("()")
    print(p)
    [x,y] = p.split(',')
    t = point(x,y)
    t.valid()
    
# make an array of points (str)
# declare a polygon
# loop through the points array and turn them into numbers for the polynomial object
    # generate an x, y pair (numerical not str) from getNumeric
    # add to the polynomial (call add_point())

print(Poly) # this should print the entire linked list of points as string
        


