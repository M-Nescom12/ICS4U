

class char:
    def __init__(self, c : str):
        self.ch = c[0]
        self.next = None
   
    def __str__(self):
        return self.ch

class myStr:
    def __init__(self, s: str):
        self.__s = s
        self.__head = char(self.__s[0])
        chCount = 1
        for c in self.__s:
            if chCount == 1:
                self.__head.next = char(c)
                self.__C = self.__head.next
            else:
                self.__C.next = char(c)
                self.__C = self.__C.next
            chCount += 1
        self.__len = chCount
       
    def length(self):
        return (self.__len - 1)
         
    def __str__(self):
        self.__C = self.__head.next
        myStr = ""
        while self.__C != None:
            myStr = myStr + self.__C.ch
            self.__C = self.__C.next
        return myStr
       
    def isacii_low(self):
        dwStr = ""
        for x in self.__s:
            c = ord(x)
            if 64 < c < 91:
                c = c + 32
            dwStr = dwStr + chr(c)
        return dwStr
        
    def isacii_high(self):
        upStr = ""
        for x in self.__s:
            c = ord(x)
            if 96 < c < 123:
               c = c - 32
            upStr = upStr + chr(c)
        return upStr


# Driver code
S = myStr("Hello world")
print(S.length())
print(S)
print(S.isacii_low())
print(S.isacii_high())
