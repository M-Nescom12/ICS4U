progname = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in."
x = progname
print(x)
def spacecounter(x):
  space = 0
  for c in range(len(x)):
    if x[c] == ' ':
      space += 1
  return space

print("Total number of spaces:", spacecounter(x))
user = input("Input characters of any kind and all spaces in data inputed will be counted:")
x = str(user)
print("Total number of spaces:", spacecounter(x))
