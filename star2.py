import turtle
screen=turtle.Screen()
c=turtle.Turtle()
c.pensize(5)
c.begin_fill()
for i in range(5):
 c.fd(200)
 c.right(144)
 c.fd(200)
 c.left(72)
 if(i==2):
 	c.color('red')
 	c.end_fill()
 	c.color('black')
turtle.done()
