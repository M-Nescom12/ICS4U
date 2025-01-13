class Polynomial:
    def __init__(self, func):
        self.__func = func
        self.__len = len(func)
        self.__EQ = ""
        
    def polycraft(self):
        i = 0
        for c in self.__func:
            if i == 0 and c < 0:
                c = c *-1
                self.__EQ = self.__EQ + "-"
            elif c < 0:
                c = c*-1
                
            if c == 0:
                pass

            elif c == 1:
                if self.__len-1 == i:
                    self.__EQ = self.__EQ + str(c)
                elif (self.__len -2) == i:
                    self.__EQ = self.__EQ + 'x'
                else:
                    piece = "x^" + str(self.__len -i-1) 
                    self.__EQ = self.__EQ + piece
            else:
                if self.__len-1 == i:
                    self.__EQ = self.__EQ + str(c)
                elif (self.__len -2) == i:
                    piece = str(c) + 'x' 
                    self.__EQ = self.__EQ + piece
                else:
                    piece = str(c) + "x^" + str(self.__len -i-1) 
                    self.__EQ = self.__EQ + piece
                    
            if i > self.__len-2:
                pass
            elif self.__func[i+1] < 0 and c != 0:
                self.__EQ = self.__EQ + " - "
            elif self.__func[i+1] > 0 and c != 0:
                self.__EQ = self.__EQ + " + "

            i += 1
        return self.__EQ
    
    def polysolver(self):
        pass

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
print(test.polycraft())
