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
        self.valid()
        
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
                
    def distance(self, p2):
        [x2,y2] = p2.get_coordinates()
        return (math.sqrt((self.__x - x2)**2 + (self.__y - y2)**2))
    
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
        self.__side_lens = []
        self.__angles = []
        self.__nodes = []

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
            
    def perimeter(self):
        Sum = 0
        side = self.__head
        dist = side.distance(side.next)
        self.__side_lens.append(dist)
        side = side.next
        while side != self.__head:
            dist = side.distance(side.next)
            self.__side_lens.append(dist)
            side = side.next
        #print(side_lens)
        for x in self.__side_lens:
            Sum = Sum + x
        return Sum
    
    def internal_angle(self):
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
                self.__angles.append(theta2)
                
            [x1, y1] = vert.get_coordinates()
            [x2, y2] = vert.next.get_coordinates()
            [x3, y3] = vert.next.next.get_coordinates()
            dotV = float((x1-x2)*(x3-x2)) + ((y1-y2)*(y3-y2))  
            mag_sum = abs(math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2)))*(math.sqrt(((x3 - x2)**2) + ((y3 - y2)**2)))
            
            if mag_sum != 0:
                theta = (math.acos((dotV/mag_sum)))*(180/math.pi)
                self.__angles.append(theta)
                vert = vert.next
            else:
                print("No duplicate points...")
                exit()
        return self.__angles
    
    def poly_check(self):
        for i in range(len(self.__angles)):
            if self.__side_lens[i] != self.__side_lens[i+1] or self.__angles[i] != self.__angles[i+1]:
                return False
        return True
        
   
    def area(self):
        print(self.__angles, self.__side_lens)
        sum1 = 0
        sum2 = 0
        if self.poly_check() == True:
            print("Regular")
            n = self.__sides
            s = self.__side_lens[0]
            Area = (n*((s)**2))/(4*(math.tan((180/n))))
        else:
            print("Irregular")
            x_points = []
            y_points = []
            V = self.__head
            self.__nodes.append(V)
            V = V.next # Moving to the next node from the head of the lsit
            while V != self.__head:
                self.__nodes.append(V)
                V = V.next
            for n in range(len(self.__nodes)):
                A, B = self.__nodes[n].get_coordinates() 
                x_points.append(A)
                y_points.append(B)
                if n == range(len(self.__nodes)):
                    A, B = self.__nodes[0].get_coordinates()  
                    x_points.append(A)
                    y_points.append(B)
            for n in range((len(self.__nodes))-1):
                sum1 += x_points[n] * y_points[n+1]
                sum2 += x_points[n+1] * y_points[n]
            Area = sum1-sum2
            Area = abs(Area/2)
        
        return Area
    
    
    def drawPoly(self):
        turtle.shape("circle")
        turtle.shapesize(0.3,0.3)
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
        V = self.__head
        nodes = str(V)  # Appending the head point to nodes
        V = V.next # Moving to the next node from the head of the lsit
        while V != self.__head:
            nodes += " -> "
            nodes += str(V)
            V = V.next
        return nodes 
