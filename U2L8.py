import math

# Part 1
A = [3, 2, 0, -1]
B = [5, 7, 8, 4]
c = [0, 0, 0, 0]

def addV(arr1, arr2):
  add = []
  for x in range (len(arr1)):
    num = int(arr1[x]) + int(arr2[x])
    add.append(num)
  return add
  
def magV(arr1, arr2):
  mag1 = []
  mag2 = []
  i = 0
  z = 0
  for x in range(len(arr1)):
    val1 = math.pow(float(arr1[x]), 2)
    val2 = math.pow(float(arr2[x]), 2)
    mag1.append(val1)
    mag2.append(val2)
  for x in range(len(mag1)):
    i = i + float(mag1[x])
    z = z + float(mag2[x])
  M = float(math.sqrt(i)) + float(math.sqrt(z))
  return M

test = addV(A, B)

if (magV(A, B)) != (magV(test, c)):
  print("The sum of the magnitudes of differnt Vectors does not\nequal the magnitude of the sum of the differnt Vectors\n")
else: 
  print("The sum of the magnitudes of differnt Vectors equals\nthe magnitude of the sum of the differnt Vectors\n")

print("The resultant Vector of adding each Vector is:\n", test)  
print("The Sum of the Magnitudes of each Vector is:\n {:.2f}".format(magV(A, B)))
print("The Magnitude after adding each Vector is:\n {:.2f}".format(magV(test, c)))

# Part 2
def cosV(arr1, arr2):
  dot = 0
  m1 = []
  m2 = []
  a = 0
  b = 0
  for x in range (len(arr1)):
    num = int(arr1[x])*int(arr2[x])
    dot = dot + num
  for x in range(len(arr1)):
    v1 = math.pow(float(arr1[x]), 2)
    v2 = math.pow(float(arr2[x]), 2)
    m1.append(v1)
    m2.append(v2)
  for x in range(len(m1)):
    a = a + float(m1[x])
    b = b + float(m2[x])
  M = float(math.sqrt(a))*float(math.sqrt(b))
  rad = float(math.acos((dot/M)))
  angle = rad*(math.pi/180)
  return angle

print("\n\nThe angle between the 2 vectors is:\n", cosV(A, B), "\n\n")

# Part 3
def dotV(arr):
  dot = 0
  for x in range (len(arr)):
    num = float(arr[x])*float(arr[x])
    dot = dot + num
  return dot
  
def sqrM(arr):
  mA = 0
  m1 = []
  for x in range(len(arr)):
    v1 = math.pow(float(arr[x]), 2)
    m1.append(v1)
  for x in range(len(m1)):
    mA = mA + float(m1[x])
  M = math.pow(float(math.sqrt(mA)), 2)
  return M

if dotV(A) == sqrM(A):
  print("The formula, A dot A = |A|^2, is always true...") 
print("The dot product between Vector A and Vector A:\n", dotV(A))
print("The magnitude of Vector A squared:\n", sqrM(A))

user = input("Do you want to know why? (Yes/No)")
user = str(user)
if user == 'Yes' or user == 'yes':
  print("\nOkay, here's how it works:\n")    
  print("The formual for the angle between 2 vectors:")
  print("cos x = (Vector1 dot Vector 2) / ( |Vector1| x |Vector2| )")
  print("The angle between 2 identical vectors is 0 degrees...")
  print("The cos of 0 degrees is 1...")
  print("And the dot product between A and A = |A|^2 ...")
  print("A number divided by itself is always 1!")
