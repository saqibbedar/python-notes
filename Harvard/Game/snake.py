import turtle
import random
import time

delay = 0.1
score = 0
heighScore = 0

#SnakeBody
bodies = []

#Getting a screen
GameScreen = turtle.Screen()
GameScreen.title("Snake Game")
GameScreen.bgcolor("gray")
GameScreen.setup(width=600, height=600)

#create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.goto(0, 200)
food.st()

#score board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("Score: 0 | High Score: 0")

def moveUp():
    if head.direction != "down":
        head.direction = "up"
    if head.direction != "up":
        head.direction = "down"
    if head.direction != "right":
        head.direction = "left"
    if head.direction != "left":
        head.direction = "right"


