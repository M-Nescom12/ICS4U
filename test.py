"""
Title: Assignment 1 - Random Magic Squares
Author: Muntasir Nathalia 
Date: Oct 23, 2024
Course: ICS 4U0

"""

""" Imported Libraries """
import random # Importing library 'Random' to randomize matricies


""" Global Variable Dictionary """
usr = input("Please enter a prime number between 5 and 19:") 
# Intializing variable 'usr' to store users input 
pri = 0 # Initializing variable with value 0 to call upon in checking if 'usr' is prime
num = [] # Initializing variable as an array to call upon in Function 2
mult = [] # Initializing variable as an array to call upon in Function 3
M1 = [] # Initializing variable as an array to return first matrix 
M2 = [] # Initializing variable as an array to return second matrix
M3 = [] # Initializing variable as an array to return third matrix


""" Function 1 """
# Function determines weather a sqaure matrix is magic or not
def isMagic(M): # Defining function 'isMagic' with pirameter 'M' (2D Array) 

# Local Variable Dictionary for Function 'isMagic'
  n = len(M) # Initializing variable as the integer value for length of array 'M'
  mnum = sum(M[0]) # Initializing variable as the integer value of the sum of All values 
                   # in the 0th/first row of the 2D Array 'M' 
  Nd = 0 # Initializing variable with value 0 to check the normal diagonal sum later on
  Id = 0 # Initializing variable with value 0 to check the inverse diagonal sum later on
  
# Checking if square is magic by checking the sums of all rows, columns, and diagnols 
  for a in range(len(M)): # looping through 'a' which is 0 to 1 less than length of array 'M'
    Hsm = 0 # Initialiazing and resetting variable for the sums of rows in 2D array 'M'
    Vsm = 0 # Initialiazing and resetting variable for the sums of columns in 2D array 'M'
    Hsm = sum(M[a]) # Storing the sum of the row 'a' of 2D array 'M' in 'HSM'
    for x in range(n): # looping through 'x' which is the range of variable 'n'
                       # (0 to 1 less than n)
      Vsm += M[x][a]  # Storing the sum of the columns by Incrementing 
                      # (Adding variable value on the right to the left value) in a for loop
                      # in a for loop to check all columns 
    if Vsm != mnum or Hsm != mnum: # Checking if all rows and columns do not add to the same sum
      return False  
    Nd = Nd + M[a][a] # Storing the sum of the values in the normal diagonal
    Id = Id + M[a][n-a-1] # Storing the sum of the values in the inverse diagonal
  if Nd != mnum or Id != mnum: # Checking if the sum of diagonals do not equal 'mnum'
    return False 
  print("The magic number for this sqaures is",mnum)  
  return True # returning true (boolean function) if square is magical

""" Function 2 """
# Function for creating a random magic array using the values 1 to 'usr' 
def create1(N): # Defining function 'create1' with pirameter 'N' (Input from user)

# A loop to randomly generate an array from 1 to N
  while True: 
    for x in range(N): 
      rand = random.randint(1,x+1) # storing a number from 1 to N that is randomized 
      if rand in num: # Checking if the number randomly generated is in the array
         pass 
      else: 
        num.append(rand) # Appending the number stored in 'rand' to array 'num'
    if len(num) == (N): # breaking loop When the desired length of the array is reached 
      break 
    
# Creating the first magic square using the randomly arranged array 'num'    
  for i in range(N): # looping through 0 to N to create a new array for each line
    ln = [] # Initializing and resseting variable for an array for each line in the square
    for n in range(len(num)): # looping through length of 'num' to shift inidices of values of 'num'
      ln.append(num[ ((n + (N-(2*i))) %N) ]) 
      # Taking the last 2 numbers in the array num and moving them to the front of array 'ln' 
      # and shifting the other values over by 2. This is done by taking users input, 'N',
      # subtracting 2 then moding by 'N' the small n is to shift the indicies value by 1 for
      # the next value in array. the 2*i is to make it that every line in the array after the 
      # 1st is shifting correctly for every line
    M1.append(ln) 
  return M1 # returning first magic square (array of arrays or 2D array)

""" Function 3 """
#  
def create2(N): #
  arr = [] # 

#
  while True: #
    for x in range(N): #
      rand = random.randint(0,x+1) #
      if rand in mult: #
         pass #
      else: #
        mult.append(rand) #
    if len(mult) == (N): #
      break #
   #

#
  for i in range(len(mult)): #
    n = int(mult[i])*N #
    arr.append(n) #
  for i in range(N): #
    ln = [] #
    for n in range(len(arr)): #
      x = ((n+(N-(3*i)))%N) #
      ln.append(arr[x]) #
    M2.append(ln) #
  return M2 #

""" Function 4 """
#
def create3(sq1, sq2): #

#
  for i in range(len(sq1)): #
    arr = [] #
    for x in range(len(sq2)): #
      a = sq1[i][x] + sq2[i][x] #
      arr.append(a) #
    M3.append(arr) #
  return M3 #
  
""" Function 5 """
#
def magic_sum(N): #
  return (N * (N**2 + 1)) / 2 #
  
  
""" Taking and Validating Input """
#
try: #
    usr = int(usr) #
    if isinstance(usr, int): #
      usr = int(usr) #
except ValueError: #
    print("You did not enter an integer...") #
    exit() #
    
#
if 4 < usr < 20: #
  for n in range(usr): #
    n = n +1 #
    if (usr%n) == 0: #
      pri = pri + 1 #
  if pri != 2: #
    print("That is not a prime number!") #
    exit() #
else: #
  print("You did not enter a number in the given range...") #
  exit() #


""" Proving the Formula and Engaging User """
print("The magic sum using the fromula is:", (magic_sum(usr)))
#
yes = input("Would you like to see for yourself? (Yes/No)")
#
if yes == 'No' or yes == 'no': #
  exit() #


""" Outputting Matricies and Their Magic Sum"""
for x in range(len(create1(usr))): #
  print(M1[x]) #
if (isMagic(M1)) == True: #
  print("It is a magic square!") #

for x in range(len(create2(usr))): #
  print(M2[x]) #
if (isMagic(M2)) == True: #
  print("It is a magic square!") #
    
for x in range(len(create3(M1, M2))): #
  print(M3[x]) #
if (isMagic(M3)) == True: #
  print("It is a magic square!") #
else: 
  print("It is not a magic square. T_T") #
