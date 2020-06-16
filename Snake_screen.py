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

window.mainloop()

#Head of the snake:
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.colour("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food of snake
apple = turtle.Turtle()
apple.speed(5)
apple.shape("circle")
apple.colour("red")
apple.penup()
apple.goto(0,0)
apple.direction = "stop"


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
    if head.distance(food) < 20:
        #random coordinate for food
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)
    snakeMoving()
    time.sleep(delay)
window.mainloop()
