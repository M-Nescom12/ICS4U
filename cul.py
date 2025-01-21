import math

class Polynomial:
    def __init__(self, func):
        self.__func = func
        self.__len = len(func)
        self.__Eq = ""
    
    def craft(self):
        i = 0
        for c in self.__func:
           
            if i == 0 and c < 0:
                c = c *-1
                self.__Eq = self.__Eq + "-"
            elif 0 < i < self.__len and c > 0 and self.__Eq != "":
                self.__Eq = self.__Eq + " + "
            elif 0 < i < self.__len and c < 0 and self.__Eq != "":
                self.__Eq = self.__Eq + " - "
                c = c*-1
                 
            if c == 0:
                pass

            elif c == 1:
                if self.__len-1 == i:
                    self.__Eq = self.__Eq + str(c)
                elif (self.__len -2) == i:
                    self.__Eq = self.__Eq + 'x'
                else:
                    piece = "x^" + str(self.__len -i-1)
                    self.__Eq = self.__Eq + piece
            else:
                if self.__len-1 == i:
                    self.__Eq = self.__Eq + str(c)
                elif (self.__len -2) == i:
                    piece = str(c) + 'x'
                    self.__Eq = self.__Eq + piece
                else:
                    piece = str(c) + "x^" + str(self.__len -i-1)
                    self.__Eq = self.__Eq + piece
           
            i += 1
        return self.__Eq
   
    def get_order(self):
        i = 0  
        while i < self.__len:
            if self.__func[i] != 0:  
                return self.__len - i - 1
            i += 1
        return -1
   
    def f(self, x: float):
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
            
    def __str__(self):
        return f"{self.__Eq}"
import math
from Polynomial import *

class IVT:
    def __init__(self, func):
        self.__func = func
        self.__len = len(func)
        self.__Poly = Polynomial(func)
        
    def solve(self, x: float, y: float):
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
   
    def derive(self, der, x: float):
        val = 0.0
        for i in range(len(der)):
            exp = len(der) - i - 1
            val = val + der[i] * (x**exp)
        return val
    
    def newton(self, x1: float):
        valid = 1e-10
        max = 100
        test = 0
        der = self.derivative()

        for __ in range(max):
            fx = self.solve(x1, 0)
            fx_pr = self.derive(der, x1)

            if fx_pr == 0:  #Failsafe
                return None
            
            if __ == max - 1: #Did not converge
                return None
            
            new_x = x1 - fx / fx_pr
            if abs(new_x - x1) < valid:
                return new_x
            x1 = new_x
        return None

    def brute(self, x1: float, x2: float):
        valid = 1e-5  
        f_x1 = self.__Poly.f(x1)
        f_x2 = self.__Poly.f(x2)
        
        if f_x1 * f_x2 > 0:
            return None

        while abs(x2 - x1) > valid:
            avg = (x1 + x2) / 2
            f_z = self.__Poly.f(avg)

            if abs(f_z) < valid:
                return avg
            elif f_x1 * f_z < 0:  
                x2 = avg
                f_x2 = f_z
            else:  
                x1 = avg
                f_x1 = f_z

        return None  

            
    def findZero(self, _x1: float, _x2: float):
        if _x1 == _x2:
            return("The x values must be different")
        elif _x1 > _x2:
            x1 = _x2
            x2 = _x1
        else:
            x1 = _x1
            x2 = _x2
            
        z1 = self.brute(x1, x2)  
        z2 = self.newton(x1)
        z3 = self.newton(x2)
        deg = self.__Poly.get_order()
        roots = []
        
        if z1 is None and z2 is None and z3 is None:
            return "No roots between given x values"
        
        elif round(z2, 9) == round(z3, 9):
            if x1-0.1 < z2 < x2+0.1 and x1 - 0.1 < z3 < x2 + 0.1:
                return z2
        
        elif deg == 2:
            if x1-0.1 < z2 < x2+0.1 and x1 - 0.1 < z3 < x2 + 0.1:
                return z2, z3
            
            elif x1-0.1 < z2 < x3 +0.1:
                return z2
            
            elif x1 - 0.1 < z3 < x2 + 0.1:
                return z3
            
            else:
                return "No root between given x values"
        
        else:
            roots.append(z2) #Root closest to negative infinity
            roots.append(z3) #Root closest to positive infinity
            i = 0
            while i < deg-2:
                low = 1/(deg-1)
                high = 1-low
                z = self.newton((z2 * high + z3 * low)) #Finds a zero thats not already found
                f = 0
                for r in roots:
                    if z is None or r is None:
                        pass
                    elif round(r, 5) == round(z, 5):
                        f = 1
                if f != 1 and z is not None:
                    roots.append(z)
                    z2 = z
                    
                else:
                    z = self.newton((z2 * 0.7 + z3 * 0.3)) #Finds a zero thats not already found in middle
                    f = 0
                    for r in roots:
                        if z is None or r is None:
                            pass
                        elif round(r, 5) == round(z, 5):
                            f = 1
                    if f != 1 and z is not None:
                        roots.append(z)
                        z2 = z        
                    else:
                        z = self.newton(((z2+z3) / 2)) #Finds a zero thats not already found closer to z3
                        f = 0
                        for r in roots:
                            if z is None or r is None:
                                pass
                            elif round(r, 5) == round(z, 5):
                                f = 1
                        if f != 1 and z is not None:
                            roots.append(z)
                            z2 = z
                                            
                        else:
                            z = self.brute((z2 + 1e-4), (z3 - 1e-4)) #Brute only works if odd zeroes in between z2 and z3
                            if z != None:
                                roots.append(z)
                                z2 = z
                i += 1
            roots.sort()
            for c in range(len(roots)):
                if x1 > roots[c] > x2:
                    roots.pop(c)
                    
            if roots == []:
                return "No root between given x values"
            return roots
          from IVT import *
from Polynomial import *

func = []
# funky = [-2,5,-3,0] or [1, -21, 175, -735, 1624, -1764, 720, 0] or [1,-10,35,-50,24 // ,0]
usr = input("Enter all coeffecients seperated by commas: ")
usr = str(usr)

digits = usr.strip("()[]{}+")
floaty = digits.split(',')

for c in floaty:
    try:
        func.append(float(c))
    except ValueError:
        print(c)
        print("Please enter NUMBERS seperated by commas...")
        exit()

Poly = Polynomial(func)
Poly.craft()
print(Poly)

x1 = input("Please input a point before the root in the function: ")
x2 = input("Please input a point after the root in the function: ")
try:
    x1 = float(x1)
    x2 = float(x2)
except ValueError:
    print("Enter a value for x1, and x2")
    exit()

Zero = IVT(func)
print(Zero.findZero(x1, x2))
from IVT import *
from Polynomial import *

func = []
# funky = [-2,5,-3,0] or [1, -21, 175, -735, 1624, -1764, 720, 0] or [1,-10,35,-50,24 // ,0]
usr = input("Enter all coeffecients seperated by commas: ")
usr = str(usr)

digits = usr.strip("()[]{}+")
floaty = digits.split(',')

for c in floaty:
    try:
        func.append(float(c))
    except ValueError:
        print(c)
        print("Please enter NUMBERS seperated by commas...")
        exit()

Poly = Polynomial(func)
Poly.craft()
print(Poly)

x1 = input("Please input a point before the root in the function: ")
x2 = input("Please input a point after the root in the function: ")
try:
    x1 = float(x1)
    x2 = float(x2)
except ValueError:
    print("Enter a value for x1, and x2")
    exit()

Zero = IVT(func)
print(Zero.findZero(x1, x2))

from Polynomial import *
func = []
usr = input("Enter all coeffecients wihtout proceeding 0s: ")
usr = str(usr)
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
print(test)

