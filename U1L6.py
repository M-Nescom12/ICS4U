# Importig math library to call upon functions
import math

year = input("Please input the year you were born: ")
year = int(year)
age = 2024-year
doub = (year*2) +5
fiftyx = doub+age
div = (fiftyx - 250) /100

print("You are",age, "years old  - You were born in the year",year,"- Double your birth year plus 5 is",doub,"- That times 50 plus your age is: ",fiftyx,"- That -250 then divided by 100 is",div)
