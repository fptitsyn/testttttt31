from turtle import *
k = 3
left(90)
tracer(0)
x, y = xcor(), ycor()

for i in range(2):
    x += 5 * k
    y += 15 * k
    goto(x, y)
    x += 111 * k
    y += 0 * k
    goto(x, y)
    x += -60 * k
    y += -15 * k
    goto(x, y)
    x += -56 * k
    y += 0 * k
    goto(x, y)

up()
for x in range(-200, 200):
    for y in range(-200, 200):
        goto(x * k, y * k)
        dot(3)

done()