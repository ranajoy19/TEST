
import turtle
LinkedIn = turtle.Turtle()
LinkedIn.speed(3)
LinkedIn.color('blue')
LinkedIn.pensize(10)
LinkedIn.begin_fill()
for i in range(4):
    LinkedIn.forward(200)
    LinkedIn.left(90)
LinkedIn.end_fill()
LinkedIn.penup()
LinkedIn.forward(100)
LinkedIn.right(90)
LinkedIn.forward(40)
LinkedIn.color('white')
LinkedIn.write('in',move=False,align="center",font=('Century Gothic',180,'bold'))
turtle.done()    


