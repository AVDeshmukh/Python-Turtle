import turtle
screen=turtle.Screen()
c=turtle.Turtle()
c.goto(30.901699437494742, 46.352549156242113)
c.pensize(5)
c.speed(0)
c.begin_fill()
for i in range(5):
 c.fd(100)
 c.right(144)
 c.fd(100)
 c.left(72)
c.color('red')
c.end_fill()
c.fd(100)
c.left(108)
c.color('navy')
c.circle(138.86617201070263)
c.right(108)
c.fd(100)
c.left(101.35101492328081)
c.circle(235.50828778708617)
turtle.done()
