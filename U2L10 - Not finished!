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
  sm1 = 0
  sm2 = 0
  sm3 = 0
  n = len(M)
  mnum = sum(M[0]) 
  for r in M:        
    if sum(r) != mnum:
      return False
    x = int(M[r][n])
    sm1 = sm1 + x
    if sm1 != mnum:
      return False 
    y = int(M[r][r])
    sm2 = sm2 + y
    if sm2 != mnum:
      return False   
    z = int(M[r][n-r-1]) 
    sm3 = sm3 + z
    if sm != mnum:
      return False     
  return True

m1 = [2, 7, 6]
m2 = [9, 5, 1]
m3 = [4, 3, 8]
M = [m1, m2, m3] # magic square

print(isMagic(M))
print("", addM(m1, m1),"\n", addM(m2, m2), "\n", addM(m3, m3))

M[0]= addM(m1, m1)
M[1]= addM(m2, m2)
M[2]= addM(m3, m3)

print(isMagic(M))
