a = [7, 1, 3, 5, 2, 4, 6]
b = []

for num in range (len(a)):
  x = ((num + 5) % 7)
  into = a[x]
  b.append(into)
  

print("Before:", a)
print("After:", b)
