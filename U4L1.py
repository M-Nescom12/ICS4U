""""
for a in range(1, 101, 1):
    for b in range(1, 101, 1):
        for c in range(1, 101, 1):
            left = a**2 + b**2
            right = c**2
            if left == right:
                print((a, b, c))

print()
"""

ulim = input("Please enter am integer to be the upper limit of the algorithim: ")
a = 3
try: 
    ulim = int(ulim) 
    if isinstance(ulim, int): 
      pass
except ValueError: 
    print("You did not enter an integer...") 
    exit() 

for a in range (3, ulim +1):
  n = int(a**2)
  if (n % 4) == 0:
    b = (n/4) - 1
    c = (n/4) + 1
  if (a % 2) != 0:
    i = int(a/2)
    b = i*(a+1)
    c = b + 1
  left = a**2 + b**2
  right = c**2
  if left == right:
    print("(%d, %d, %d)" % (a, b, c))

