import math

class Polynomial:
    def __init__(self, func):
        self.__func = func
        self.__len = len(func)
        self.__EQ = ""
        self.__derive = []
       
    def polycraft(self):
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
   
    def polysolve(self, x, y):
        i = 0
        val = 0.0
        while i < self.__len:
            exp = self.__len - i - 1
            val = val + self.__func[i] * (x**exp)
            i += 1
        return val - y
   
    def polyderive(self, funky):
        derive = []
        i = 0
        while i < self.__len:
            exp = self.__len - i - 1
            if exp > 0 and funky[i] != 0:
                derive.append(funky[i]*exp)
            i += 1
        return derive
   
    def derivative(self, der, x):
        val = 0.0
        for i in range(len(der)):
            exp = len(der) - i - 1
            val = val + der[i] * (x**exp)
        return val
   
    def f(self, x):
        i = 0
        y = 0.0
        if self.get_order() == 0:
            return "Every number from positive infinity to negative infinity"
        elif self.get_order() > 0:
            for c in self.__func:
                if i == self.__len-1:
                    y = y + c
                elif i == self.__len-2:
                    y = x*c + y
                else:
                    y = x**(self.__len-(i+1))*c+y
                i += 1
            return y
   
    def polyfind__x(self, y):
        x = 0  
        valid = 0.001  
        Max = 100  
        test = 0
        r = None
        r1 = None
        r2 = None
        der = self.polyderive(self.__func)
        deg = self.get_order()
       
        if deg == -1:
            print("No function found")
            exit()
        elif deg == 0:
            r = ("Every number from positive infinity to negative infinity")
        elif deg == 1:
            r = (x - self.__func[self.__len-1])/der[0]
        elif deg == 2:
            a = self.__func[self.__len-3]
            b = self.__func[self.__len-2]
            c = self.__func[self.__len-1] - y
           
            Qf = (b**2 - 4*a*c)
            print(Qf)
            if Qf > 0:
                r1 = (-1*b + math.sqrt(Q))/(2*a)
                r2 = (-1*b - math.sqrt(Q))/(2*a)
            elif Qf == 0:
                r = (-1*b)/(2*a)
                if r == 0:
                    r = abs(r)
        elif deg > 2:
            while test < Max:
                fx = self.polysolve(x, y)
                fx_pr = self.derivative(der, x)  

                if fx_pr == 0:
                    print("Math Error")
                    break
               
                new_x = x - fx / fx_pr
               
                if abs(new_x - x) < valid:
                    r = new_x
                    break

                x = new_x
                test += 1

        if r is None and (r1 is None or r2 is None):
            print("Not Found")
        elif r2 != None:
            return r1, r2
        else:
            return r
   
    def polyzeroes(self, x1, x2):  
        root = None
        root2 = None
        der = self.polyderive(self.__func)
        deg = self.get_order()
       
        if deg == -1:
            print("No function found")
            exit()
        elif deg == 0:
            r = ("Every number from positive infinity to negative infinity")
        elif deg == 1:
            r = (x - self.__func[self.__len-1])/der[0]
        elif deg == 2:
            a = self.__func[0]
            b = self.__func[1]
            c = self.__func[2] - y
           
            Qf = (b**2 - 4*a*c)/a
            if Qf > 0:
                r2 = -1*b + math.sqrt(Q)
                r2 = -1*b - math.sqrt(Q)
               
        elif deg > 2:
            pass

        if root is None:
            print("Not Found")
        elif root2 != None:
            return root1, root2
        else:
            return root
        
    def __str__(self):
        return f"{self.__EQ}"
