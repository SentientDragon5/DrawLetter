import turtle
pen = turtle.Turtle()
pen.hideturtle()

def a(x,y,size):
    skip = False
    a = [
        ("l"),
        (x,y - size*1),
        (x + size*2,y - size*1),
        (x + size*2,y - size*4),
        (x,y - size*4),
        (x,y - size*2),
        (x + size*2,y - size*2)
        ]
    for num in a:
        if skip == True:
            pen.up(); pen.goto(num); pen.down()
        skip = False
        if num == "l":
            skip = True
        else:
            pen.goto(num)

a(0,0,10)
        
#(x,y),
