import turtle
import time
import random

delay = 0.1

#Setting up the screen
window = turtle.Screen()
window.title("Snake Game by Lexiang Pan and Ryan Shen")
window.bgcolor("green")
window.setup(width=600, height = 600)
window.tracer(0)

#Head of the snake:
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food of snake
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0,100)
apple.direction = "stop"

segments = []

#functions
def going_up():
    head.direction = "up"
def going_down():
    head.direction = "down"
def going_left():
    head.direction = "left"
def going_right():
    head.direction = "right"

#Functions
def snakeMoving():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard Binding
window.listen()
window.onkeypress(going_up, "w")
window.onkeypress(going_down, "s")
window.onkeypress(going_left, "a")
window.onkeypress(going_right, "d")

while True:
    window.update()

    #check for collision 
    if head.distance(apple) < 20:
        #move food to a new coordinate
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        apple.goto(x, y)

        #add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)
    
    #moving the end segments first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #moving segments to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    snakeMoving()
    time.sleep(delay)

window.mainloop()
