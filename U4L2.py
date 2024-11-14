import turtle

def modify(ln):
  mod_string = ""
  badChars = ['"', ','] 
  ln = ln.strip() 
  for c in ln:
    if c not in badChars:
      mod_string = mod_string + c
  return mod_string 

def symbols(ln):
  Rfile = []
  mod_string = ""
  badChars = ['"', ',', ' '] 
  ln = ln.strip()
  for c in ln:
    if c not in badChars:
      mod_string = c
      Rfile.append(mod_string)
    elif c == ' ':
      mod_string = '\\'
      Rfile.append(mod_string)
  return Rfile 

fh = open("smiley_emoji_mod.xpm", "r") 
color_data = fh.readline()
color_data = modify(color_data)
[cols, rows, colors] = color_data.split()
rows = int(rows)
cols = int(cols)
colors = int(colors)

colorData = {} 

for i in range(colors):
  cLine = fh.readline()
  cLine = modify(cLine)
  [sym, c, color] = cLine.split()
  colorData[sym] = color 

def writeDot(obj, rad, color):
  obj.pendown()
  obj.dot(rad, color)
  obj.penup()

t = turtle.Turtle()
turtle.bgcolor("gray40")
turtle.tracer(0, 0)
t.hideturtle()

t.penup()
t.forward((-1*cols)//2)
t.left(90)
t.forward(rows//2)
t.right(90)
t.pendown()

for y in range(rows):
  fl = fh.readline()
  xmp = symbols(fl)
  for x in range(cols):
    if xmp[x] in colorData:
      writeDot(t, 4, colorData[xmp[x]])
      t.forward(1)
    else:
      print(f"Warning: Undefined symbol '{xmp[x]}' at row {y}, col {x}")
  t.forward(-1*(rows-1))
  t.right(90)
  t.forward(1)
  t.left(90)
print("The number of rows:", rows)
print("The number of columns:", cols)
print("The number of colors:", colors)
for color in colorData.values():
  print(color)
