import turtle

t = turtle.Turtle()
t.fillcolor('blue')
t.begin_fill()
t.pensize(10)
t.right(90)
t.forward(50)
for n in[
  (30,200), (90,200), (30,50)
]:
    t.circle(n[0], 180)
    t.forward(n[1])
t.right(90)
t.forward(60)
t.end_fill()

t.penup()
t.goto(0, 100)
t.pendown()
t.fillcolor('cyan')
t.begin_fill()
for i in range(2):
  t.forward(50)
  t.circle(40, 180)
t.end_fill()

t.penup()
t.goto(-125, 120)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
t.left(180)
t.forward(25)
t.left(90)
t.forward(125)
t.left(90)
t.forward(25)
t.end_fill()