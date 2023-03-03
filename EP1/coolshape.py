import turtle
t = turtle.Pen()
t.shape("turtle")
t.color("blue")
t.pensize(5)

for i in range(12):
    t.left(30)
    for i in range(12):
        t.forward(100)
        t.left(30)

t.done()
