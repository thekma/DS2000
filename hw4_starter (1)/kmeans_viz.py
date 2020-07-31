# DO NOT CHANGE ANYTHING IN THIS FILE
# USED TO VISUALIZE K-MEANS MAIN PROGRAM

import turtle

# Sets a few Turtle parameters
def setup(minx, miny, maxx, maxy, turtlespeed):
    turtle.setworldcoordinates(minx, miny, maxx, maxy)
    turtle.speed(turtlespeed)
    turtle.hideturtle()

# Waits for the user to close a window
def wait():
    turtle.textinput('', 'Press esc to Continue.')

# Waits for the user to click the window,
# then exits
def done():
    title("Done - Waiting for Click")
    turtle.exitonclick()

# Sets the window title
def title(s):
    turtle.title(s)

# Clears the window
def clear():
    turtle.clear()

# Draws a centroid as a cross
def draw_centroid(color, x, y):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y-1)
    turtle.pendown()
    turtle.goto(x, y+1)
    turtle.penup()
    turtle.goto(x-1, y)
    turtle.pendown()
    turtle.goto(x+1, y)

# Draws a list of centroids
def draw_centroids(centroids):
    for c in centroids:
        draw_centroid(c[0], c[1][0], c[1][1])

# Draws a point with a color
def draw_point(color, x, y):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot()

# Draws a whole dataset given each point's
# assigned centroid
def draw_assignment(centroids, assignment):
    for i in range(len(centroids)):
        for p in assignment[i]:
            draw_point(centroids[i][0], p[0], p[1])
