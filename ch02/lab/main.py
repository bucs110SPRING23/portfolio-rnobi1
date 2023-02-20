import random
import turtle 
import math
import pygame

#part 1
window = turtle.Screen
window = turtle.screensize(200,200)

#creating the turtle
vicky = turtle.Turtle()    
lemon = turtle.Turtle()
vicky.color('black')
lemon.color('blue')
vicky.shape('turtle')
lemon.shape('turtle')

#pick up the pen
vicky.up() 
lemon.up()

#create start and finish line
vicky.goto(-100,50)
vicky.write("Start")
vicky.pendown()
vicky.goto(-100,-40)
vicky.penup()                 
vicky.goto(-60,50)
vicky.write("Finish Line")
vicky.pendown()
vicky.goto(-60,-40)
vicky.penup()

#getting turtles ready for race
vicky.color("orange")
vicky.goto(-100,20)
lemon.goto(-100,-20)

#race 1
vicky.forward(50)
lemon.forward(60)
vicky.goto(-100,20)
lemon.goto(-100,-20)

#race 2
for turn in range(10):
  vicky.forward(random.randrange(0,10))
  lemon.forward(random.randrange(0,10))
vicky.goto(-100,20)
lemon.goto(-100,-20)

turtle.exitonclick()

#part 2
pygame.init()
window = pygame.display.set_mode() 

points = []
side_length = 20
xpos = 0
ypos = 0
for sides in range(4):
    num_sides = 4
    angle = 360/num_sides
    radians = math.radians(angle * sides)
    x = int(xpos + side_length * math.cos(radians))
    y = int(ypos + side_length * math.sin(radians))
    points = [x, y]
    pygame.draw.polygon(window, 'green', points)
    pygame.display.flip()

pygame.quit()