import random

from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=700)
user_bet = screen.textinput(title= "Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "blue", "orange", "yellow", "green", "purple", "AliceBlue", "aquamarine", "brown", "DarkBlue", "cyan"]
y_position = [-330, -264, -198, -132, -66, 0, 66, 132, 198, 264, 330]
all_turtles = []

for turtle_index in range(0,11):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-480, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 480:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()