from turtle import *
from random import *
s = Screen()
s.title(' + @ ')
w, h = 700, 700
s.setup(w, h)
s.bgcolor('black')
star = Turtle()
star.shape('circle')
star.shapesize(0.05,0.05)
star.color('white')
star.pu()
star.speed(6)  
for i in range(150):
    x = randint(-w/2, w/2)  
    cycle = Turtle()
cycle.ht()  
cycle.speed(0)
cycle.color('white')
cycle.pu()
cycle.pensize(2)
radius = 5  
acc_ext = 0  
for i in range(1000):
    extent = random() * 90  
    color = choice([(1,1,1),(0/255, 0/255, 0/255)])  
    cycle.color(color)
    cycle.circle(radius, extent)
    acc_ext += extent  
    if acc_ext > 360:  
        acc_ext = 0
        radius += 3
        cycle.penup()
        cycle.goto(0,-radius)  
        cycle.pendown()  
        cycle.setheading(0)
