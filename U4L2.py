import turtle

def modify(ln):
  mod_string = ""
  badChars = ['"', ','] 
  ln = ln.strip() 
  for c in ln:
    if c not in badChars:
      mod_string = mod_string + c
  return mod_string 

def symbols(ln, file):
  Rfile = []
  mod_string = ""
  badChars = ['"', ',', ' '] 
  ln = ln.strip()
  for c in ln:
    if c not in badChars:
      mod_string = c
      Rfile.append(mod_string)
    elif c == ' ' and file == "teapot_mod.xpm":
      mod_string = '~'
      Rfile.append(mod_string)
    elif c == ' ' and file == "smiley_emoji_mod.xpm":
      mod_string = '\\'
      Rfile.append(mod_string)
    elif c == ' ' and file == "cool_smiley_mod.xpm":
      mod_string = '~'
      Rfile.append(mod_string)
  return Rfile 

def writeDot(obj, rad, color):
  obj.pendown()
  obj.dot(rad, color)
  obj.penup()
  
usr = input("Enter 1 for smiley emoji, 2 for cool emoji, and 3 for teapot: ")
usr = int(usr)
if usr == 1:
  f = "smiley_emoji_mod.xpm"
if usr == 2:
  f = "cool_smiley_mod.xpm"
if usr == 3:
  f = "teapot_mod.xpm"
  
fh = open(f, "r") 
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
  xpm = symbols(fl, f)
  for x in range(len(xpm)):
    if xpm[x] in colorData:
      writeDot(t, 4, colorData[xpm[x]])
      t.forward(1)
    else:
      print(f"Warning: Undefined symbol '{xpm[x]}' at row {y}, col {x}")
  t.forward(-1*(len(xpm)))
  t.right(90)
  t.forward(1)
  t.left(90)
print("The number of rows:", rows)
print("The number of columns:", cols)
print("The number of colors:", colors)
for color in colorData.values():
  print(color)
