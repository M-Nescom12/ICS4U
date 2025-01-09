Funky = [-2,5,-3,-1]
usr = input("Enter all coeffecients wihtout proceeding 0s: ")
usr = str(usr)
x1 = input("Please input a point before the root in the function: ")
x2 = input("Please input a point after the root in the function: ")
try:
    x1 = float(x1)
    x2 = float(x2)
except ValueError:
    print("Enter a value for x1, and x2")
    
digits = usr.strip("()[]{}")
floaty = digits.split(',')
func = []
for c in floaty:
    try:
        func.append(float(c))
    except ValueError:
        print("Please enter coeffecients seperated by commas...")
        exit()
print(func)
print(polynomial)
