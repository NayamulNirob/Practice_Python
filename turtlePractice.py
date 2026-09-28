from turtle import *
'''
Python's turtle module is a built-in library for drawing graphics with code. 
It's modeled on the "turtle graphics" idea from the Logo language: 
you control a virtual pen (the "turtle") that moves around a window, 
drawing lines as it goes.
'''

# tt = turtle.Turtle()
# turtle.title('Drawing Brod')
# turtle.bgcolor('white')
# turtle.setup(width=800, height=600)
# turtle.done()


# --- Set up the window ---
screen = Screen()
screen.title("Turtle Sample: Spiral and Star")
screen.bgcolor("black")

# --- Create the turtle ---
t = Turtle()
t.speed(0)        # 0 = fastest drawing speed
t.width(2)
t.hideturtle()    # hide the arrow icon

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta"]

# --- Draw a colorful spiral ---
for i in range(150):
    t.color(colors[i % len(colors)])  # cycle through the colors
    t.forward(i * 2)                  # each line is longer than the last
    t.left(59)                        # turn slightly less than 60 degrees

# --- Move to the center without drawing ---
t.penup()
t.goto(0, 0)
t.pendown()

# --- Draw a filled star in the middle ---
t.color("white", "gold")   # (outline color, fill color)
t.begin_fill()
for _ in range(5):
    t.forward(80)
    t.right(144)           # 144 degrees makes a 5-point star
t.end_fill()

# --- Keep the window open until it's closed ---
done()