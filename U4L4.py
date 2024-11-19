class Fraction:
    def __init__(self, num, den):
        self.__n = num
        self.__d = den
    
    def getNum(self):
        return self.__n
        
    def getDen(self):
        return self.__d
    
    def setNum(self, num):
        self.__n = num
    
    def setDen(self, den):
        self.__d = den
    
    def __str__(self):
        return "{0}/{1}".format(self.__n, self.__d)
        
class Fraction2(Fraction):
    def __init__(self, num, den):
      super().__init__(num, den)
    
    def check(self, id):
      if self.getDen() == 0:
        print("Error: The denominator is zero in fraction", id)
        exit()
        
    def reduce(self):
      num = self.getNum()
      den = self.getDen()
      i = int(num)
      if num != 0:
        while i != 1:
          if (den)%i == 0 and (num)%i == 0:
            den = den // i
            num = num // i
          i = i - 1
      self.setNum(num)
      self.setDen(den)
      
    def multiply(self, num2, den2):
      num1 = self.getNum()
      den1 = self.getDen()
      self.setNum(num1*num2)
      self.setDen(den1*den2)
      
    def unreduce(self, multiplier):
      self.setNum(self.getNum() * multiplier)
      self.setDen(self.getDen() * multiplier)  
      
    def add_f(self, num2, den2):
      num1 = self.getNum()
      den1 = self.getDen()
      new_num = (num1*den2)+(num2*den1)
      new_den = den1*den2
      self.setNum(new_num)
      self.setDen(new_den)

print("Frist Fraction:")
x = input("Please input a number for the numerator")
y = input("Please input a number for the denominator")
x = int(x) 
y = int(y)
f = Fraction2(x, y)
f.check("1") 

print("Second Fraction:")
n = input("Please input a number for the numerator")
d = input("Please input a number for the denominator")
n = int(n)
d = int(d)
j = Fraction2(n, d)
j.check("2") 

print("\n1st Fraction as is: ", f)
f.reduce()
print("The simplified fractions is: ", f)
print("\n2nd Fraction as is: ", j)
j.reduce()
print("The simplified fractions is: ", j)

f.add_f(n,d)
f.reduce()
print("\nThe sum is: ", f)
f.multiply(n,d)
f.reduce()
print("The quotient is: ", f)
