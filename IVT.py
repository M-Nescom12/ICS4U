import math

class Polynomial:
    def __init__(self, func):
        self.__func = func
        self.__len = len(func)
        self.__EQ = ""
        self.__derive = []
       
    def craft(self):
        i = 0
        for c in self.__func:
           
            if i == 0 and c < 0:
                c = c *-1
                self.__EQ = self.__EQ + "-"
            elif 0 < i < self.__len and c > 0 and self.__EQ != "":
                self.__EQ = self.__EQ + " + "
            elif 0 < i < self.__len and c < 0 and self.__EQ != "":
                self.__EQ = self.__EQ + " - "
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
           
            i += 1
        return self.__EQ
   
    def get_order(self):
        i = 0  
        while i < self.__len:
            if self.__func[i] != 0:  
                return self.__len - i - 1
            i += 1
        return -1
   
    def solve(self, x, y):
        i = 0
        val = 0.0
        while i < self.__len:
            exp = self.__len - i - 1
            val = val + self.__func[i] * (x**exp)
            i += 1
        return val - y
   
    def derivative(self):
        derive = []
        i = 0
        while i < self.__len:
            exp = self.__len - i - 1
            if exp > 0 and self.__func[i] != 0:
                derive.append(self.__func[i]*exp)
            i += 1
        return derive
   
    def derive(self, der, x):
        val = 0.0
        for i in range(len(der)):
            exp = len(der) - i - 1
            val = val + der[i] * (x**exp)
        return val
   
    def f(self, x):
        i = 0
        y = 0.0
        for c in self.__func:
            if i == self.__len-1:
                y = y + c
            elif i == self.__len-2:
                y = x*c + y
            else:
                y = x**(self.__len-(i+1))*c+y
            i += 1
        return y
   
    def x(self, y, x1, x2): 
        valid = 0.001    
        test = 0
        r = None
        der = self.derivative(self.__func)
        
        while test < x2:
            fx = self.solve(x1, y)
            fx_pr = self.derive(der, x1)  

            if fx_pr == 0:
                print("Math Error")
                break
               
            new_x = x1 - fx / fx_pr
            if abs(new_x - x1) < valid:
                r = new_x
                break

            x1 = new_x
            test += 1
        return r

   
    def findZero(self, _x1, _x2):
        deg = self.get_order()
        
        if _x1 == _x2:
            return("The x values must be different")
        elif _x1 > _x2:
            x1 = _x2
            x2 = _x1
        else:
            x1 = _x1
            x2 = _x2
        
        if deg == -1:
            return "No function found"
            
        elif deg == 0:
            r = self.__func[self.__len-1]
                
        elif deg == 1:
            r = (0 - self.__func[self.__len-1])/der[0]
            
        elif deg == 2:
            a = self.__func[self.__len-3]
            b = self.__func[self.__len-2]
            c = self.__func[self.__len-1] 
           
            Qf = (b**2 - 4*a*c)
            if Qf > 0:
                r1 = (-1*b + math.sqrt(Qf))/(2*a)
                r2 = (-1*b - math.sqrt(Qf))/(2*a)
            elif Qf == 0:
                r = (-1*b)/(2*a)
                if r == 0:
                    r = abs(r)
            else:
                return "No root found..."
            
        elif deg > 0:
            der = self.derivative(self.__func)

            
             
    def __str__(self):
        return f"{self.__EQ}"

#from Polynomial import *
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

test = Polynomial(func)
test.craft()

print("Equation: ", test)
print("Derivative: ", test.derivative())
print("Find y: ", test.f(0))
print("Find 0: ", test.findZero(x1,x2))

