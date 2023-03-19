from turtle import Turtle
import random

RANDOMINT = 10

class Helenaturtle:
    def __init__(self, shape, color, x, y, number):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y
        self.number = number

        self.turtles= []
        self.new_turtle()

    def new_turtle(self):
        for i in range(self.number):
            t = Turtle()
            t.penup()
            t.shape(self.shape)
            t.color(self.color[i])
            t.goto(self.x, self.y[i])

            self.turtles.append(t)

    def move_turtle(self):
        self.xcors = []
        for t in self.turtles:
            if t.xcor() < 380:
                t.forward(random.randint(0,RANDOMINT))
            else:
                return t.fillcolor()
            

    
class Helenawall:
    def __init__(self):
        self.w = Turtle()
        self.w.penup()
        self.w.shape("square")
        self.w.color("cyan")
        self.w.shapesize(400,1)
        self.w.goto(405,0)

class Helenatext:
    def __init__(self, message):
        self.message = message

        self.t = Turtle()
        self.t.fillcolor("white")
        self.t.color("white")
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(-100, 0)
        self.t.write(self.message, font=("Arial", 20, "normal"))