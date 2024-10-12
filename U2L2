seconds = 100
(mins, secs) = divmod(seconds, 60)
print("Length of time was: %d:%d" % (mins, secs))

secs = 10 ** 12  
(mins, sec) = divmod(secs, 60)
(hrs, min_) = divmod(mins, 60)
(days, hrs_) = divmod(hrs, 24)
(years, days_) = divmod(days, 1461) 
years *= 4 

print("One trillion seconds is the same as")
print(years, "years; ", days_, " days; ", hrs_,
      " hours; ", min_, " minutes; and ", sec, " seconds")
      
inch = 10 ** 12  
(foot, inch) = divmod(inch, 12)
(yard, foot) = divmod(foot, 3)
(mile, yard) = divmod(yard, 1760)
(moondist, mile) = divmod(mile, 238855) 

print("One trillion inches is the same as going to the moon and back") 
print(moondist,"times, plus an extra", mile,"miles,",yard,"yards,",foot,"feets, and",inch,"inches.\n")

def toLower(x):
  x = ord(x)
  if 96 < x < 123:
    print("Error: Not an uppercase letter")  
    print(" ")
  else:
    x = x + 32
    return chr(x)
while True: 
  print("Want to play the 'to lower' game?")
  user = input("Input 'Y'to play or 'N' to quit...")
  user = str(user)
  if user == 'N' or user == 'n':
    print("Goodbye!")
    break
  else:
    x = input("Please input an uppercase letter:")
    x = str(x)
    if toLower(x) != None:
      print("The lowercase of that letter is:", toLower(x))
