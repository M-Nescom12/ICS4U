import math

x = input("Please input a whole number between 1 and 20: ")
x = int(x)
y = input("Please input another nonzero whole number between 1 and 20")
y = int(y)

if 0 < y < 21 and 0 < x < 21:
  print("Now deciding if", y, "is a factor of", x, "...")
  rem = x % y 
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
  else: 
    print(y, "is not a factor of", x)
elif x == 0 or y == 0:
  print("0 is not a valid input")
else:
 print("Values must be within given range")
