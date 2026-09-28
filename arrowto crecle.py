import turtle

colors = ["red","purple", "blue","green", "yellow","orange"]

turtle.bgcolor('black')

turtle.hideturtle()
turtle.speed(3)

for x in range(360):
    turtle.pencolor(colors[x%len(colors)])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(59)

turtle.done()