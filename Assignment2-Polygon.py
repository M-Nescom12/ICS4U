import math
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def add_point(self, data):
        new_point = Node(data)
        if tail is None:
            tail = new_point
            new_point.next = new_point
        else:
            new_point.next = tail.next
            tail.next = new_point
            tail = new_point
        return tail

    def distance(self, p2):
        return math.sqrt((self.__x-p2.x)**2 + (self.__y-p2.y)**2)
class Polygon():
        

        
        
