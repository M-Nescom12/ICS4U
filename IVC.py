Funky = [-2,5,-3,-1]
usr = input("Enter all coeffecients wihtout proceeding 0s: ")
usr = str(usr)
x1 = input("Please input a point before the root in the function: ")
x2 = input("Please input a point after the root in the function: ")
func = []
a = -1

for n in range(len(usr)):
    char = usr[n]
    if char == ' ' or char == ',':
        pass
    elif char == '-':
        a = n+1
    else:    
        try:
            int(char)
            print(char)
            if a == n:
                char = char*-1
            func.append(char)
        except ValueError:
            print("Please enter integers for coefecients only")
            exit()
            
if func == []:
    print("Please enter an input...")
    exit()

print(func)
    
