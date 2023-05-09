import turtle
import random

# Set up turtle
tim = turtle.Turtle()
tim.speed('fastest')
tim.penup()
tim.goto(0, 0)
tim.pendown()

# Set up screen boundaries
screen = turtle.Screen()
screen_width = screen.window_width() // 2
screen_height = screen.window_height() // 2

# Function to flip a coin and turn the turtle
def flip_coin_and_turn():
    coin = random.choice(['heads', 'tails'])
    if coin == 'heads':
        tim.left(90)
    else:
        tim.right(90)

# Move the turtle 50 steps forward and check if it's still on the screen
while -screen_width < tim.xcor() < screen_width and -screen_height < tim.ycor() < screen_height:
    flip_coin_and_turn()
    tim.forward(50)
