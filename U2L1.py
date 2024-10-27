A = [2, 8, 6, 3, 9, 1, 7]
B = [0] * 7

# Add your code here!
for n in range(len(B)):
  B[n] = A[(n+2) %7]
  print(f"B[{n}] gets it value from A[{(n+2)%7}]")
print("B =", B) 
