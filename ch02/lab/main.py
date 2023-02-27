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
xpos = 400
ypos = 400

for sides in range(3):
  num_sides = 3
  angle = 360/num_sides
  radians = math.radians(angle * sides)
  x = int(xpos + side_length * math.cos(radians))
  y = int(ypos + side_length * math.sin(radians))
  pos = (x,y)
  points.append(pos)
window.fill([255, 255, 255])
pygame.draw.polygon(window,[0,0,0], points)
pygame.display.flip()

pygame.time.delay(1000)
window.fill([0,0,0])
pygame.display.flip()

points = []
for sides in range(4):
  num_sides = 4
  angle = 360/num_sides
  radians = math.radians(angle * sides)
  x = int(xpos + side_length * math.cos(radians))
  y = int(ypos + side_length * math.sin(radians))
  pos = (x,y)
  points.append(pos)
window.fill([255, 255, 255])
pygame.draw.polygon(window,[0,0,0], points)
pygame.display.flip()

pygame.time.delay(1000)
window.fill([0,0,0])
pygame.display.flip()

points = []
for sides in range(6):
  num_sides = 6
  angle = 360/num_sides
  radians = math.radians(angle * sides)
  x = int(xpos + side_length * math.cos(radians))
  y = int(ypos + side_length * math.sin(radians))
  pos = (x,y)
  points.append(pos)
window.fill([255, 255, 255])
pygame.draw.polygon(window,[0,0,0], points)
pygame.display.flip()

pygame.time.delay(1000)
window.fill([0,0,0])
pygame.display.flip()

points = []
for sides in range(20):
  num_sides = 20
  angle = 360/num_sides
  radians = math.radians(angle * sides)
  x = int(xpos + side_length * math.cos(radians))
  y = int(ypos + side_length * math.sin(radians))
  pos = (x,y)
  points.append(pos)
window.fill([255, 255, 255])
pygame.draw.polygon(window,[0,0,0], points)
pygame.display.flip()

pygame.time.delay(1000)
window.fill([0,0,0])
pygame.display.flip()

points = []
for sides in range(100):
  num_sides = 100
  angle = 360/num_sides
  radians = math.radians(angle * sides)
  x = int(xpos + side_length * math.cos(radians))
  y = int(ypos + side_length * math.sin(radians))
  pos = (x,y)
  points.append(pos)
window.fill([255, 255, 255])
pygame.draw.polygon(window,[0,0,0], points)
pygame.display.flip()

pygame.time.delay(1000)
window.fill([0,0,0])
pygame.display.flip()

points = []
for sides in range(360):
  num_sides = 360
  angle = 360/num_sides
  radians = math.radians(angle * sides)
  x = int(xpos + side_length * math.cos(radians))
  y = int(ypos + side_length * math.sin(radians))
  pos = (x,y)
  points.append(pos)
window.fill([255, 255, 255])
pygame.draw.polygon(window,[0,0,0], points)
pygame.display.flip()

pygame.time.delay(1000)
window.fill([0,0,0])
pygame.display.flip()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()