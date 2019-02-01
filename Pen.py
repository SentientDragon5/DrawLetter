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

#alphabetLet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'ENTER':10,'j':11,'k':12}

myStr = ['c','a','b',' ','b','a','g',' ','a','d','d','e','d']
alphabet = ['a','b','c','d','e','f','g','h','ENTER','i','j',' ','k']
placeAt = {'x':x,'y':y,'size':size}
lettLoop = 1
for char in myStr:
    
    letter = {' ':[]}
    letter['ENTER'] = [("ENTER")]
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
    
#letter['e'] = [("l"),(x + size*2,y - size*4),
