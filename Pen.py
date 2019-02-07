import turtle
pen = turtle.Turtle()
pen.hideturtle()
skip = False

#START SPOT
startx = 0
starty = 0
size = 10
x = startx
y = starty

print('size: ',size)

#alphabetLet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'`':10,'j':11,'k':12}
inStr = input('letters: abcdefghijklmnopqrstuvwxyz, ENTER = "`", SPACE = " "\nstring : ')
myStr = []
for c in range(0,len(inStr),1):
    myStr.append(inStr[c])
print (inStr , myStr)
#myStr = ['c','a','b',' ','b','a','g',' ','a','d','d','e','d']
alphabet = ['a','b','c','d','e','f','g','h','`','i','j',' ','k','l']
placeAt = {'x':x,'y':y,'size':size}
lettLoop = 1
for char in myStr:
    
    letter = {' ':[]}
    letter['`'] = [("ENTER")]
    letter['a'] = [("l"),(x,y - size*1),(x + size*2,y - size*1),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2)]
    letter['b'] = [("l"),(x,y),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*2),(x,y - size*2)]
    letter['c'] = [("l"),(x + size*2,y - size*2),(x,y - size*2),(x,y - size*4),(x + size*2,y - size*4)]
    letter['d'] = [("l"),(x + size*2,y),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2)]
    letter['e'] = [("l"),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y - size*3),(x,y - size*3)]
    letter['f'] = [("l"),(x + size,y - size*4),(x + size,y),(x + size*2,y),(x + size*2,y - size*1),("l"),(x + size*2,y - size*2),(x,y - size*2)]
    letter['g'] = [("l"),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*1),(x,y - size*1),(x,y - size*3),(x + size*2,y - size*3)]
    letter['h'] = [("l"),(x + size*2,y - size*4),(x + size*2,y - size*2),(x,y - size*2),(x,y - size*4),(x,y)]
    letter['i'] = [("l"),(x + size*2,y - size*4),(x,y - size*4),(x + size*1,y - size*4),(x + size*1,y - size*2),(x + size*2,y - size*2),(x,y - size*2),("l"),(x + size*1,y - size*1),("d")]
    letter['j'] = [("l"),(x + size*1,y - size*3),(x,y - size*3),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*1),("l"),(x + size*2,y),("d")]
    letter['k'] = [("l"),(x,y - size*4),(x,y - size*3),(x + size*2,y - size*4),(x,y - size*3),(x + size*2,y - size*2),(x,y - size*3),(x,y)]
    letter['l'] = [("l"),(x + size*1,y - size*4),(x + size*1,y)]
    letter['m'] = [("l"),(x,y - size*1),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y - size*4),("l"),(x + size,y - size*2),(x + size,y - size*4)]
    letter['n'] = [("l"),(x,y - size*1),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y - size*4)]
    letter['o'] = [("l"),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2)]
    letter['p'] = [("l"),(x,y - size*4),(x,y),(x + size*2,y),(x + size*2,y - size*2),(x,y - size*2)]
    letter['q'] = [("l"),(x + size*2,y - size*4),(x + size*2,y),(x,y),(x,y - size*2),(x + size*2,y - size*2)]
    letter['r'] = [("l"),(x,y - size*4),(x,y - size*2),(x,y - size*3),(x + size*2,y - size*2)]
    letter['s'] = [("l"),(x + size*2,y - size*2),(x,y - size*2),(x + size*2,y - size*4),(x,y - size*4)]
    letter['t'] = [("l"),(x + size,y - size*4),(x + size,y),("l"),(x + size*2,y - size*2),(x,y - size*2)]
    letter['u'] = [("l"),(x,y - size*2),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*2)]
    letter['v'] = [("l"),(x,y - size*2),(x + size,y - size*4),(x + size*2,y - size*2)]
    letter['w'] = [("l"),(x,y - size*2),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*2),("l"),(x + size,y - size*4),(x + size,y - size*2)]
    letter['x'] = [("l"),(x + size*2,y - size*4),(x,y - size*2),("l"),(x,y - size*4),(x + size*2,y - size*2)]
    letter['y'] = [("l"),(x,y),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y),(x + size*2,y - size*4),(x + size,y - size*4)]
    letter['z'] = [("l"),(x,y - size*2),(x + size*2,y - size*2),(x,y - size*4),(x + size*2,y - size*4)]


    for num in letter[char]:
        if skip == True:
            pen.up(); pen.goto(num); pen.down()
        skip = False
        if num == "d":
            pen.dot(size/2)
            skip = True
        if num == "ENTER":
            y -= size *6
            x = startx - (size *3)
            skip = True
        if num == "l":
            skip = True
        elif num == "d":
            skip = False
        elif num == "ENTER":
            skip = False
        else:
            pen.goto(num)
            
        print(num)
    x += size *3
    lettLoop += 1
print(myStr)
#letter['e'] = [("l"),(x + size*2,y - size*4),
#(x + size*2,y - size*4),
