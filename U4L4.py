class Fraction:
    # See slideshow for a full discussion of this code.
    #
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
        
# driver code
f = Fraction(3, 4)
print(f)

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

    def reduce__check(self):
      num = self.getNum()
      den = self.getDen()
      for i in range(2, num+1):
        if (den)%i == 0 and (num)%i == 0:
          while (den)%i == 0 and (num)%i == 0:
            den = den // i
            num = num // i
      self.setNum(num)
      self.setDen(den)
      
x = input("Please input a number for the numerator")
y = input("Please input a number for the denominator")
x = int(x)
y = int(y)
f2 = Fraction2(x, y)
f2.check() 
print("Fraction as is: ", f2)
unred = input("Enyter a number to multiply fraction: ")
unred = int(unred)
f2.unreduce(unred)
print(f2)
f2.reduce__check()
print(f2)
