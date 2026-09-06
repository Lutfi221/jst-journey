import turtle

turtles = []
arms = 8

for i in range(arms):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("red")
    t.speed(10)
    turtles.append(t)

for i in range(1000):
    for t in turtles:
        t.forward(1)
        t.left(360 / arms)

# Draw eye outline like < >


turtle.done()
