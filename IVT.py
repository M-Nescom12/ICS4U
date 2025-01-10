class Polynomial:
    def __init__(self, func):
        self.__func = func
        self.__len = len(func)
        self.__EQ = ""
        
    def polycraft(self):
        i = 0
        for c in self.__func:
            if self.__len-1 == i:
                self.__EQ = self.__EQ + str(c)
                print(c)
            elif (self.__len -2) == i:
                piece = str(c) + 'x' 
                self.__EQ = self.__EQ + piece
                print(c)
            else:
                piece = str(c) + "x^" + str(self.__len -i-1) 
                self.__EQ = self.__EQ + piece
                print(c)
            i += 1
        print(self.__EQ)
        
from Polynomial import *
func = []
Funky = [-2,5,-3,-1]
usr = input("Enter all coeffecients wihtout proceeding 0s: ")
usr = str(usr)
x1 = input("Please input a point before the root in the function: ")
x2 = input("Please input a point after the root in the function: ")
try:
    x1 = float(x1)
    x2 = float(x2)
except ValueError:
    print("Enter a value for x1, and x2")
    exit()
    
digits = usr.strip("()[]{}+")
floaty = digits.split(',')

for c in floaty:
    try:
        func.append(float(c))
    except ValueError:
        print("Please enter NUMBERS seperated by commas...")
        exit()
print(func)
test = Polynomial(func)
test.polycraft()
