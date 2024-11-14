import turtle

def modify(ln):
  # Strips everything except the essential string
  # ln = one line of data from first column to the carriage return
  #
  mod_string = ""
  badChars = ['"', ','] # chars to remove
  ln = ln.strip() # clean out non-printable chars
  for c in ln:
    if c not in badChars:
      mod_string = mod_string + c
  return mod_string # line of data should now be clean

def modify1(ln):
  Rfile = []
  mod_string = ""
  badChars = ['"', ','] 
  ln = ln.strip()
  for c in ln:
    if c not in badChars:
      mod_string = c
      Rfile.append(mod_string)
  return Rfile # line of data should now be clean

fh = open("smiley_emoji_mod.xpm", "r") # open a file handle
color_data = fh.readline()
color_data = modify(color_data)
[cols, rows, colors] = color_data.split()
rows = int(rows)
cols = int(cols)
colors = int(colors)

colorData = {} # a dictionary of symbols and colors

for i in range(colors):
  cLine = fh.readline()
  cLine = modify(cLine)
  [sym, c, color] = cLine.split()
  colorData[sym] = color # add a new dictionary entry
print(colorData)

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

for y in range(cols):
    xmp = [0]*cols
    if y > (colors):
        fl = fh.readline()
        fl = modify1(fl)
        xmp.append(fl)
        for x in range(rows):
            writeDot(t, 4, colorData[xmp[x]])
            t.penup()
            t.forward(1)
        t.forward(-1)
        t.forward(-1*cols)
        t.right(90)
        t.forward(2)
        t.left(90)

