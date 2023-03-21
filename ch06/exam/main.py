import turtle
import random

def main():
    window = turtle.Screen()
    window.screensize(1000,1000)
    window.bgcolor("black")

    markus = turtle.Turtle()
    markus.speed(0)
    markus.color("red", "yellow")
    markus.begin_fill()

    num_petals = random.randint(5,10)
    def draw_petals():
        return 360/num_petals
    x = draw_petals()
        
    def draw_flower(turtle, radius, angle):
        turtle.circle(radius, angle)
        turtle.left(180 - angle)
        turtle.circle(radius, angle)
        turtle.left(180 - angle)
    
    for i in range(num_petals):
        draw_flower(markus,100,80)
        markus.left(x)
    
    markus.end_fill()
    turtle.exitonclick()
main()

