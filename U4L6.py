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
        
    def __str__(self):
        self.__C = self.__head.next
        myStr = ""
        while self.__C != None:
          myStr = myStr + self.__C.ch
          self.__C = self.__C.next
        return myStr

# Driver code
S = myStr("Hello")
print(S) # should print the string

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
       
    def isacii(self):
        upStr = ""
        for x in range(self.__len):
            y = chr(myStr[x])
            y = ord(y)
            if 96 < y < 123:
                print("Error: Not an uppercase letter")  
            else:
                y = y + 32
            upStr = upStr + chr(y)
        return upStr



# Driver code
S = myStr("Hello")
print(S.length())
print(S.isacii())
print(S) # should print the string
