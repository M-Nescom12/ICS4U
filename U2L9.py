a1 = [2, 7, 6]
a2 = [9, 5, 1]
a3 = [4, 3, 8]
Magic3 = [a1, a2, a3] # an array of arrays

def IzM(arr):
  h = 0
  v = 0
  d = 0
  print("", arr[0],"\n", arr[1],"\n", arr[2])
# Horizontals
  for x in range (len(arr)):
    L1 = arr[x]
    for i in range (len(L1)):
      V1 = L1[i]
      h = h + V1
  h = float(h/3)
# Verticals
  for x in range (len(arr)):
    vert1 = arr[0][x]
    v = v + vert1
  for x in range (len(arr)):
    vert2 = arr[1][x]
    v = v + vert2
  for x in range (len(arr)):
    vert3 = arr[2][x]
    v = v + vert3
  v = float(v/3)  
# Diagnols
  for x in range (len(arr)):
    diag1 = arr[x][x]
    d = d + diag1  
  for x in range (len(arr)):
    diag2 = arr[2-x][x]
    d = d + diag2 
  d = float(d/2)
  
  m = float(h + v + d)/3
  print("Horizontals add to:",h,"\nVerticals add to:",v,"\nDiagnols add to:",d)
  
  if h == v and h == d and v == d:
    print("It is a magic square!")
    
  return m


print("\nThe magic number for a 3 by 3 magic square is:", IzM(Magic3))

# Adding a value to whole array
alladd = input("\nInput a number to add to every value of the array:")
alladd = int(alladd)

AA1 = []
for c in range (len(a1)):
  change = int(a1[c]) + alladd
  AA1.append(change)
AA2 = []
for c in range (len(a2)):
  change = int(a2[c]) + alladd
  AA2.append(change)
AA3 = []
for c in range (len(a3)):
  change = int(a3[c]) + alladd
  AA3.append(change)

Magic3[0] = AA1
Magic3[1] = AA2
Magic3[2] = AA3

print("\nThe magic number for the new square is:", IzM(Magic3))

# Subtracting a value to whole array
allsub = input("\nInput a number to subtract to every value of the array:")
allsub = int(allsub)

BB1 = []
for c in range (len(a1)):
  change = int(a1[c]) - allsub
  BB1.append(change)
BB2 = []
for c in range (len(a2)):
  change = int(a2[c]) - allsub
  BB2.append(change)
BB3 = []
for c in range (len(a3)):
  change = int(a3[c]) - allsub
  BB3.append(change)

Magic3[0] = BB1
Magic3[1] = BB2
Magic3[2] = BB3

print("\nThe magic number for the new square is:", IzM(Magic3))

# Multiplying a value to whole array
allmult = input("\nInput a number to multiply to every value of the array:")
allmult = int(allmult)

CC1 = []
for c in range (len(a1)):
  change = int(a1[c]) * allmult
  CC1.append(change)
CC2 = []
for c in range (len(a2)):
  change = int(a2[c]) * allmult
  CC2.append(change)
CC3 = []
for c in range (len(a3)):
  change = int(a3[c]) * allmult
  CC3.append(change)

Magic3[0] = CC1
Magic3[1] = CC2
Magic3[2] = CC3

print("\nThe magic number for the new square is:", IzM(Magic3))