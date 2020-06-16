import turtle
import time

delay = 0.1

#Setting up the screen
window = turtle.Screen()
window.title("Snake Game by Lexiang Pan and Ryan Shen")
window.bgcolor("green")
window.setup(width=600, height = 600)
window.tracer(0)

window.mainloop()

#Head of the snake:

snakeHead = turtle.Turtle()
head.speed(5)
head.shape("circle")
head.colour("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Function
def going_up():
    head.direction = "up"
def going_down():
    head.direction = "down"
def going_left():
    head.direction = "left"
def going_right():
    head.direction = "right"

#snake moving 
def snakeMoving():
    if head.direction == "up":
        yCoordinate = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        yCoordinate = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        yCoordinate = head.ycor()
        head.setx(x - 20)   
    if head.direction == "right":
        yCoordinate = head.ycor()
        head.setx(x + 20)

#Keyboard Binding
window.listen()
window.onkeypress(going_up, "w")
window.onkeypress(going_down, "s")
window.onkeypress(going_left, "a")
window.onkeypress(going_right, "d")



#Snake head on screen
while True:
    window.update()

    snakeMoving()
    time.sleep(delay)
window.mainloop()
