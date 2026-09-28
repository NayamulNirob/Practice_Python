"""
Turtle Showcase: "Night Village"
================================
A scene that uses most of what Python's turtle module offers:

  * drawing: forward/left/goto/circle/dot/begin_fill/end_fill/write
  * colors: RGB tuples (colormode 255), hex strings, color names
  * animation: tracer(0) + update() + ontimer()
  * a second turtle with a real turtle shape, stamps and pen up/down
  * keyboard and mouse events

Run it with:   python turtle_night_village.py
Controls:
  Arrow keys  move / turn the turtle     SPACE  stamp the turtle
  P           pen up / pen down          C      random turtle color
  F           grow a flower              Click  add a star
  Q           quit
"""

import math
import random
import tkinter
import turtle

# ------------------------------------------------------------------ #
# 1. SCREEN SETUP
# ------------------------------------------------------------------ #
WIDTH, HEIGHT = 900, 650
HORIZON = -100                       # y-coordinate where ground begins

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Turtle Showcase - Night Village")
screen.colormode(255)                # lets us use (r, g, b) tuples
screen.bgcolor((11, 16, 38))
screen.tracer(0)                     # draw instantly; we call update() ourselves

pen = turtle.Turtle()                # the "artist" that draws the scene
pen.hideturtle()
pen.speed(0)

running = True


# ------------------------------------------------------------------ #
# 2. DRAWING HELPERS
# ------------------------------------------------------------------ #
def jump(x, y):
    """Move without drawing a line."""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def rect(x, y, w, h, color):
    """Filled rectangle; (x, y) is the bottom-left corner."""
    jump(x, y)
    pen.setheading(0)
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(w)
        pen.left(90)
        pen.forward(h)
        pen.left(90)
    pen.end_fill()


def circle_at(x, y, radius, color):
    """Filled circle centered on (x, y)."""
    jump(x, y - radius)              # turtle.circle() starts at the bottom
    pen.setheading(0)
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def polygon(points, color):
    """Filled polygon from a list of (x, y) points."""
    pen.color(color)
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()


def star(x, y, size, color):
    """Five-point star centered on (x, y); size = length of each line."""
    radius = size / (2 * math.sin(math.radians(72)))
    offset = radius * math.cos(math.radians(72))
    jump(x - size / 2, y + offset)
    pen.setheading(0)
    pen.color(color)
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()


PETAL_COLORS = ["#ff8fab", "#ffc2d1", "#ffd6a5", "#caffbf", "#bde0fe", "#e0bbe4"]


def flower(x, y, petals=10, size=30):
    """A flower made from lens-shaped petals."""
    jump(x, y)
    pen.setheading(0)
    pen.pensize(1)
    pen.pencolor((255, 255, 255))
    for _ in range(petals):
        pen.fillcolor(random.choice(PETAL_COLORS))
        pen.begin_fill()
        pen.circle(size, 60)         # arc
        pen.left(120)
        pen.circle(size, 60)         # second arc closes the petal
        pen.left(120)
        pen.end_fill()
        pen.left(360 / petals)       # rotate to the next petal
    pen.dot(size * 0.6, "#ffd60a")   # golden center


def write_text(x, y, text, size, color, font="Georgia", style="normal"):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.write(text, align="left", font=(font, size, style))


# ------------------------------------------------------------------ #
# 3. SCENE PIECES
# ------------------------------------------------------------------ #
def sky_color(y):
    """Blend from purple at the horizon to deep navy at the top."""
    t = (y - HORIZON) / (HEIGHT / 2 - HORIZON)
    t = max(0.0, min(1.0, t))
    top, bottom = (11, 16, 38), (92, 58, 110)
    return tuple(int(bottom[i] + (top[i] - bottom[i]) * t) for i in range(3))


def draw_sky():
    y = HEIGHT / 2
    while y > HORIZON - 10:          # stack thin bands to fake a gradient
        rect(-WIDTH / 2 - 20, y - 6, WIDTH + 40, 7, sky_color(y))
        y -= 6


def draw_stars(count=90):
    for _ in range(count):
        jump(random.randint(-440, 440), random.randint(20, 315))
        pen.dot(random.choice([2, 2, 3, 4]),
                random.choice(["white", "#fff2b0", "#cfe6ff"]))
    for x, y, size in [(-380, 150, 14), (-60, 200, 12), (120, 270, 18)]:
        star(x, y, size, (255, 242, 176))


def draw_moon(x, y, r):
    circle_at(x, y, r + 30, (38, 40, 78))     # outer glow
    circle_at(x, y, r + 15, (58, 60, 105))    # inner glow
    circle_at(x, y, r, "#f6f1c7")
    for dx, dy, cr in [(-14, 10, 8), (12, -6, 6), (-2, -22, 5)]:
        circle_at(x + dx, y + dy, cr, "#e2dbaa")   # craters


def draw_mountains():
    dark, mid = (38, 32, 74), (46, 38, 86)
    polygon([(-500, HORIZON), (-380, 90), (-260, HORIZON)], dark)
    polygon([(-330, HORIZON), (-180, 150), (-30, HORIZON)], mid)
    polygon([(60, HORIZON), (220, 120), (380, HORIZON)], mid)
    polygon([(250, HORIZON), (400, 70), (520, HORIZON)], dark)
    # snow caps
    polygon([(-180, 150), (-156, 110), (-168, 118), (-180, 105),
             (-192, 118), (-204, 110)], (225, 230, 245))
    polygon([(220, 120), (242, 84), (231, 92), (220, 80),
             (209, 92), (198, 84)], (225, 230, 245))


def draw_ground():
    rect(-WIDTH / 2 - 20, -HEIGHT / 2 - 20, WIDTH + 40,
         HORIZON + HEIGHT / 2 + 20, (22, 48, 40))
    rect(-WIDTH / 2 - 20, HORIZON - 8, WIDTH + 40, 8, (34, 72, 52))


def pine(x, y, scale=1.0):
    rect(x - 6 * scale, y, 12 * scale, 30 * scale, (70, 45, 35))
    for i in range(3):               # three stacked triangles
        w = (60 - i * 14) * scale
        base = y + (22 + i * 34) * scale
        polygon([(x - w / 2, base), (x, base + 50 * scale), (x + w / 2, base)],
                (24 + i * 6, 90 + i * 12, 60 + i * 4))


def window(x, y, size=32):
    rect(x - 4, y - 4, size + 8, size + 8, (200, 150, 70))   # warm glow
    rect(x, y, size, size, (255, 214, 102))
    pen.color((120, 70, 40))
    pen.pensize(2)
    jump(x + size / 2, y)
    pen.goto(x + size / 2, y + size)
    jump(x, y + size / 2)
    pen.goto(x + size, y + size / 2)
    pen.pensize(1)


def draw_house():
    rect(-80, -85, 16, 45, (110, 60, 50))                        # chimney
    for px, py, pr in [(-72, -30, 7), (-64, -12, 9), (-54, 10, 11)]:
        circle_at(px, py, pr, (150, 140, 170))                   # smoke
    rect(-195, -210, 150, 100, (150, 84, 60))                    # walls
    polygon([(-210, -110), (-120, -40), (-30, -110)], (90, 40, 50))  # roof
    rect(-130, -210, 28, 55, (70, 40, 30))                       # door
    jump(-107, -183)
    pen.dot(5, "gold")                                           # door knob
    window(-185, -170)
    window(-90, -170)


def draw_fireflies(count=25):
    for _ in range(count):
        jump(random.randint(-430, 430), random.randint(-320, -120))
        pen.dot(random.choice([3, 4, 5]), (255, 240, 130))


def build_scene():
    random.seed(42)                  # same scene every run
    draw_sky()
    draw_stars()
    draw_moon(300, 220, 45)
    draw_mountains()
    draw_ground()
    for x, y, s in [(-400, -250, 1.1), (-330, -230, 1.3),
                    (300, -210, 1.0), (120, -230, 1.2), (200, -260, 1.5)]:
        pine(x, y, s)
    draw_house()
    for x, y, n, size in [(-320, -280, 8, 16), (-40, -300, 10, 14),
                          (330, -285, 9, 18)]:
        flower(x, y, n, size)
    draw_fireflies()
    write_text(-440, 268, "Night Village", 30, (255, 240, 200),
               style="bold italic")
    write_text(-440, 245, "Arrows: move/turn   SPACE: stamp   P: pen up/down",
               10, (200, 200, 230), font="Courier")
    write_text(-440, 230, "C: color   F: flower   Click: add a star   Q: quit",
               10, (200, 200, 230), font="Courier")
    random.seed()                    # back to real randomness


# ------------------------------------------------------------------ #
# 4. THE HERO TURTLE (controlled with the keyboard)
# ------------------------------------------------------------------ #
hero = turtle.Turtle(shape="turtle")
hero.color((60, 200, 120), (30, 140, 80))    # (outline, body)
hero.shapesize(2, 2, 2)                      # stretch width, length, outline
hero.pensize(3)
hero.speed(0)
hero.penup()
hero.goto(150, -285)


def random_color():
    return (random.randint(80, 255), random.randint(80, 255),
            random.randint(80, 255))


def go_forward():
    hero.forward(15)
    screen.update()


def go_back():
    hero.backward(15)
    screen.update()


def turn_left():
    hero.left(15)
    screen.update()


def turn_right():
    hero.right(15)
    screen.update()


def stamp_hero():
    hero.stamp()                     # leaves a copy of the turtle behind
    screen.update()


def toggle_pen():
    if hero.isdown():
        hero.penup()
    else:
        hero.pendown()
    screen.title("Turtle Showcase - pen is " + ("DOWN" if hero.isdown() else "UP"))


def change_color():
    hero.color(random_color(), random_color())
    screen.update()


def grow_flower():
    x, y = hero.position()           # the artist pen draws it where the hero stands
    flower(x, y, random.choice([6, 8, 10, 12]), random.randint(14, 24))
    screen.update()


def add_star(x, y):
    star(x, y, random.randint(12, 28), random_color())
    screen.update()


def quit_app():
    global running
    running = False
    screen.bye()


# ------------------------------------------------------------------ #
# 5. ANIMATION: a shooting star that streaks across the sky
# ------------------------------------------------------------------ #
comet = turtle.Turtle(shape="circle")
comet.hideturtle()
comet.penup()
comet.color((255, 255, 210))
comet.speed(0)
comet_state = {"x": -400.0, "y": 300.0, "trail": [], "wait": 0}


def launch_comet():
    comet_state["x"] = random.randint(-450, -100)
    comet_state["y"] = random.randint(150, 320)
    comet_state["trail"] = []
    comet_state["wait"] = random.randint(20, 80)   # frames to pause first


def animate_comet():
    if not running:
        return
    try:
        s = comet_state
        if s["wait"] > 0:
            s["wait"] -= 1
        else:
            s["x"] += 11
            s["y"] -= 4.5
            s["trail"] = (s["trail"] + [(s["x"], s["y"])])[-14:]
            comet.clearstamps()
            for i, (px, py) in enumerate(s["trail"]):
                comet.goto(px, py)
                comet.shapesize(0.05 + i * 0.035)   # tail tapers off
                comet.stamp()
            if s["x"] > 470 or s["y"] < 40:
                comet.clearstamps()
                launch_comet()
        screen.update()
        screen.ontimer(animate_comet, 40)           # run again in 40 ms
    except (turtle.Terminator, tkinter.TclError):
        pass                                        # window was closed


# ------------------------------------------------------------------ #
# 6. START EVERYTHING
# ------------------------------------------------------------------ #
build_scene()
launch_comet()
screen.update()

screen.onkeypress(go_forward, "Up")
screen.onkeypress(go_back, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkey(stamp_hero, "space")
screen.onkey(toggle_pen, "p")
screen.onkey(change_color, "c")
screen.onkey(grow_flower, "f")
screen.onkey(quit_app, "q")
screen.onscreenclick(add_star)
screen.listen()                      # start listening for key presses

animate_comet()
turtle.done()                        # keep the window open


# ------------------------------------------------------------------ #
# QUICK REFERENCE: turtle commands
# ------------------------------------------------------------------ #
# Movement : forward/fd, backward/bk, left/lt, right/rt, goto/setpos,
#            setx, sety, setheading/seth, home, circle(r, extent, steps),
#            dot(size, color), stamp, clearstamp, clearstamps, undo
# Pen      : penup/pu, pendown/pd, pensize/width, pencolor, fillcolor,
#            color, begin_fill, end_fill, filling
# State    : position/pos, xcor, ycor, heading, towards, distance,
#            isdown, isvisible
# Looks    : shape, shapesize, hideturtle/ht, showturtle/st, speed,
#            write, clear, reset
# Screen   : setup, title, bgcolor, colormode, tracer, update, ontimer,
#            onkey, onkeypress, onscreenclick, listen, textinput,
#            numinput, done/mainloop, exitonclick, bye
