def factorize(x):
  a = 0
  for i in range(1, x + 1):
    if x % i == 0 and i != x:
      a = a + i
  return(a) 
  
n = input("Please input a number:")
n = int(n)
check = factorize(n)
print("Factor Sum: ", check)

if check == n:
  print(n,"is perfect")
  
if check > n:
    print(n, "is abundant")
  
if check < n:
   print(n,"is defecient")
