
from turtle import Turtle, Screen
import random

is_race_on = False
screen= Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title = "Guess the turtle", prompt= "Which turtle's gonna win?")

colors = ['red', 'orange', 'green', 'yellow', 'blue', 'purple', 'chocolate']
y_positions = [0,40,80,120,-40,-80, -120]
turtles = []

for i in range(7):
    new_chitti = Turtle(shape='turtle')
    new_chitti.color(colors[i])
    new_chitti.penup()
    new_chitti.goto(-230, y_positions[i])
    turtles.append(new_chitti)

if user_choice :
    is_race_on = True

while is_race_on :

    for chitti in turtles :
        if chitti.xcor() > 230 :
            is_race_on = False
            winning_color = chitti.pencolor()
            if winning_color == user_choice :
                print(f"You've won! The {winning_color} chitti is the winner")
            else :
                print(f"You've lost the race and the winner is {winning_color} color chitti")
        rand_dist = random.randint(0,10)
        chitti.fd(rand_dist)


screen.exitonclick()
