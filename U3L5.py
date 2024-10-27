import math

def add(a, b):
  return a + b
  
x = input("Please input a number:")
y = input("Please input a number:")


try:
    x = int(x)
    y = int(y)

    if isinstance(x, int) and isinstance(y, int):
        print(add(x, y))
    else:
        print("Not a valid input")
except ValueError:
    print("Not a valid input")
