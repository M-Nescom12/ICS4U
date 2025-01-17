import math

class Polynomial:
    def __init__(self, func):
        self.__func = func
        self.__len = len(func)
        self.__eq = ""
        self.__derive = []
       
    def craft(self):
        i = 0
        for c in self.__func:
           
            if i == 0 and c < 0:
                c = c *-1
                self.__eq = self.__eq + "-"
            elif 0 < i < self.__len and c > 0 and self.__eq != "":
                self.__eq = self.__eq + " + "
            elif 0 < i < self.__len and c < 0 and self.__eq != "":
                self.__eq = self.__eq + " - "
                c = c*-1
                 
            if c == 0:
                pass

            elif c == 1:
                if self.__len-1 == i:
                    self.__eq = self.__eq + str(c)
                elif (self.__len -2) == i:
                    self.__eq = self.__eq + 'x'
                else:
                    piece = "x^" + str(self.__len -i-1)
                    self.__eq = self.__eq + piece
            else:
                if self.__len-1 == i:
                    self.__eq = self.__eq + str(c)
                elif (self.__len -2) == i:
                    piece = str(c) + 'x'
                    self.__eq = self.__eq + piece
                else:
                    piece = str(c) + "x^" + str(self.__len -i-1)
                    self.__eq = self.__eq + piece
           
            i += 1
        return self.__eq
   
    def get_order(self):
        i = 0  
        while i < self.__len:
            if self.__func[i] != 0:  
                return self.__len - i - 1
            i += 1
        return -1
   
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
   
    def newton(self, x1: float):
        valid = 0.0001
        max = 100
        test = 0
        der = self.derivative()
       
        for __ in range(max):
            fx = self.solve(x1, 0)
            fx_pr = self.derive(der, x1)

            if fx_pr == 0:  
                return None
            
            if __ == max - 1:
                return None
            
            new_x = x1 - fx / fx_pr
            if abs(new_x - x1) < valid:
                return new_x
            x1 = new_x
        return None

    def brute(self, x1: float, x2: float):
        valid = 1e-5  
        f_x1 = self.f(x1)
        f_x2 = self.f(x2)

        if f_x1 * f_x2 > 0:
            return None

        while abs(x2 - x1) > valid:
            avg = (x1 + x2) / 2
            f_z = self.f(avg)

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
            a = self.__func[self.__len - 3]
            b = self.__func[self.__len - 2]
            c = self.__func[self.__len - 1]
           
            Qf = (b**2 - 4 * a * c)
            if Qf > 0:
                r1 = (-1 * b + math.sqrt(Qf))/(2 * a)
                r2 = (-1 * b - math.sqrt(Qf))/(2 * a)
            elif Qf == 0:
                r = (-1 * b)/(2 * a)
                if r == 0:
                    r = abs(r)
            else:
                return "No root found..."
           
        elif deg > 2:
            # 3 of x zeroes
            if self.newton(x1) != None:
                r1 = round(self.newton(x1), 5)
                print(r1)
            if self.newton(x1) != None:
                r2 = round(self.newton(x2), 5)
                print(r2)
            if self.brute(x1, x2) != None:
                r3 = round(self.brute(x1, x2), 5)
                print(r3)
                
                # Recursion tomorrow for all possible zeroes
            xb1 = r1 - 0.1
            xb2 = r1 + 0.1
                
            xb3 = r2 - 0.1
            xb4 = r2 + 0.1
        
            for n in range(int(xb2), int(xb3)):
                print(1, xb3, xb2)
                ch = self.brute(xb2,xb3)
                if self.brute(xb2,xb3) == None:
                    xb3 = xb3-1
                else:
                    print(ch)
            
            while (self.brute(x1, xb1) != None) or (self.brute(xb2, xb3) != None) or (self.brute(xb4, x2) != None):
                print(1)
                z = []
                if self.brute(x1, xb1) != None:
                    z.append(self.brute(x1, xb1)) # Before 1st
                    x1 = z[0] + 0.1
                        
                elif self.brute(xb2, ab3) != None:
                    z.append(self.brute(xb2, xb3)) # Between 1s and 2nd
                    xb2 = z[0] + 0.1
                        
                elif self.brute(xb4, x2) != None:
                    z.append(self.brute(xb4, x2)) # After last
                    xb4 = z[0] + 0.1
                        
                elif z == []:
                    print("Nope!")
                    break
                print(z)
                    
                    
            # One zero only
            z1 = self.newton(x1)
            if z1 is None or abs(self.f(z1)) > 1e-5:  
                z2 = self.newton(x2)
                if z2 is None or abs(self.f(z2)) > 1e-5 != 0:
                    z3 = self.brute(x1, x2)
                    if z3 is None or abs(self.f(z3)) > 1e-5 != 0:
                        return "No roots between given values"
                    elif round(z1, 5) != 0:
                        return round(z3, 5)
                    else:
                       return 0.0 
                elif round(z1, 5) != 0.0:
                    return round(z2, 5)
                else:
                    return 0.0
            elif round(z1, 5) != -0.0:        
                return round(z1, 5)
            else:
                return 0.0
            
    def __str__(self):
        return f"{self.__eq}"
 
#from Polynomial import *
func = []
Funky = [-2,5,-3,0]
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

print(test)
print("Find y: ", test.f(0))
print("Zero at x = ", test.findZero(x1,x2))
