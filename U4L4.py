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
    
    def check(self):
      if self.getDen() == 0:
        print("Error: The denominator is zero.")
        exit()
            
    def unreduce(self, multiplier):
      self.setNum(self.getNum() * multiplier)
      self.setDen(self.getDen() * multiplier)
        
    def reduce(self):
      num = self.getNum()
      den = self.getDen()
      i = int(num)
      while i != 1:
        if (den)%i == 0 and (num)%i == 0:
          den = den // i
          num = num // i
        i = i - 1
      self.setNum(num)
      self.setDen(den)
      
x = input("Please input a number for the numerator")
y = input("Please input a number for the denominator")
try: 
    x = int(x) 
    y = int(y)
    if isinstance(x, int): 
      pass
    if isinstance(y, int):
      pass
except ValueError: 
    print("You did not enter an integer...") 
    exit()
f = Fraction2(x, y)
f.check() 
print("Fraction as is: ", f)

unred = input("Enyter a number to multiply fraction: ")
unred = int(unred)
f.unreduce(unred)
print("The unreduced fraction is", f)
f.reduce()
print("The simplified fractions is", f)
