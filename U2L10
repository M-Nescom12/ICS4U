# Functions
def addM(M1, M2):
  i = 0
  C = []
  for num in range (len(M1)):
    x = int(M1[num])
    y = int(M2[num])
    values = x + y
    C.append(values)
    i = i + 1
  return C

def isMagic(M):
  n = len(M)
  x = 0
  y = 0
  z = 0
  nd = 0
  id = 0
  mnum = sum(M[0]) 
  for a in range(len(M)): 
    x = x + M[a][0]
    y = y + M[a][1]
    z = z + M[a][2]
    nd = nd + M[a][a]
    id = id + M[a][n-a-1]
    print(M[a])
    if sum(M[a]) != mnum:
      return False
  if x != mnum or y != mnum or z != mnum or nd != mnum or id != mnum:
    return False
  return True
  
# Original Matrix
m1 = [2, 7, 6]
m2 = [9, 5, 1]
m3 = [4, 3, 8]
M = [m1, m2, m3] # magic square

#A) Add to itself Matrix
print("Itself")
M[0]= addM(m1, m1)
M[1]= addM(m2, m2)
M[2]= addM(m3, m3)
print(isMagic(M))

#B) Value added to All Matrix
print("\nAll add value")
user = input("Input a number to add to the Matrix:")
alnum = [user, user, user]
M[0]= addM(m1, alnum)
M[1]= addM(m2, alnum)
M[2]= addM(m3, alnum)
print(isMagic(M))

#C) Adding Matrix to Rotation
print("\nRotated")
M = [m1, m2, m3]
c1 = [0, 0, 0]
c2 = [0, 0, 0]
c3 = [0, 0, 0]
CM = [c1, c2, c3]
for i in range(len(M)):
  CM[2][i] = M[i][0]  
  CM[1][i] = M[i][1]  
  CM[0][i] = M[i][2] 
M[0]= addM(m1, c1)
M[1]= addM(m2, c2)
M[2]= addM(m3, c3)
print(isMagic(M))

#D) Reflection Sum Matrix
print("\nReflected")
M = [m1, m2, m3]
r1 = [0, 0, 0]
r2 = [0, 0, 0]
r3 = [0, 0, 0]
RM = [r1, r2, r3]
for i in range(len(M)):  
    RM[i][0] = M[i][2] 
    RM[i][1] = M[i][1]
    RM[i][2] = M[i][0]
M[0]= addM(m1, r1)
M[1]= addM(m2, r2)
M[2]= addM(m3, r3)
print(isMagic(M))

#E) Transposed Matrix
print("\nTransposed:")
M = [m1, m2, m3]
t1 = [0, 0, 0]
t2 = [0, 0, 0]
t3 = [0, 0, 0]
TM = [t1, t2, t3]

for x in range(len(M)):
  for i in range(len(M)):
    TM[x][i] = M[i][x]
M[0]= addM(m1, t1)
M[1]= addM(m2, t2)
M[2]= addM(m3, t3)
print(isMagic(M))
