import turtle

window = turtle.Screen
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.color("blue")

user_sides = int(input("How many sides are in your shape? "))
user_len = int(input("How long are each side? "))

for i in range(user_sides):
    turtle.forward(user_len)
    turtle.left(360/user_sides)