import turtle
pen = turtle.Turtle()
pen.hideturtle()
skip = False

#START SPOT
x = 0
y = 0
size = 10
print(size)

alphabetLet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'ENTER':10,'j':11,'k':12}
alphabetNum = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'ENTER',11:'j',12:'k'}
placeAt = {'x':x,'y':y,'size':size}
lettLoop = 1
for lettnum in alphabetLet:
    print(alphabetNum[lettLoop])
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

    for num in letter[lettnum]:
        if skip == True:
            pen.up(); pen.goto(num); pen.down()
        skip = False
        if num == "d":
            pen.dot(size/2)
        if num == "ENTER":
            y -= size *6
        if num == "l" or "d" or"ENTER":
            skip = True
        else:
            pen.goto(num)
        print(num)
    x += size *3
    lettLoop += 1
#letter['e'] = [("l"),(x + size*2,y - size*4),
