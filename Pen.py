import turtle
pen = turtle.Turtle()
pen.hideturtle()
skip = False

#START SPOT
x = 0
y = 0
size = 2
print(size)

alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
alphabetNum = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g'}
placeAt = {'x':x,'y':y,'size':size}
lettLoop = 1
for lettnum in alphabet:
    print(alphabetNum[lettLoop])
    letter = {'a':[("l"),(x,y - size*1),(x + size*2,y - size*1),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2)]}
    letter['b'] = [("l"),(x,y),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y - size*2),(x,y - size*2),]
    letter['c'] = [("l"),(x + size*2,y - size*2),(x,y - size*2),(x,y - size*4),(x + size*2,y - size*4)]
    letter['d'] = [("l"),(x + size*2,y),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2)]
    letter['e'] = [("l"),(x + size*2,y - size*4),(x,y - size*4),(x,y - size*2),(x + size*2,y - size*2),(x + size*2,y - size*3),(x,y - size*3)]
    letter['f'] = [("l"),(x + size,y - size*4),(x + size,y),(x + size*2,y),(x + size*2,y - size*1),("l"),(x + size*2,y - size*2),(x,y - size*2)]
    letter['g'] = [("l"),(x,y - size*4),(x + size*2,y - size*4),(x + size*2,y),(x,y),(x,y - size*2),(x + size*2,y - size*2)]

    for num in letter[lettnum]:
        if skip == True:
            pen.up(); pen.goto(num); pen.down()
        skip = False
        if num == "l":
            skip = True
        else:
            pen.goto(num)
        print(num)
    x += size *3
    lettLoop += 1
