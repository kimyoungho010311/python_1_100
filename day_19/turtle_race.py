from turtle import Turtle, Screen
import random 

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Whitch turtle win the race? Enter a color in rainbow : ")
colors = ['red','orange','yellow','green','blue','purple']

turtles = []

for i in range(5):
    t = Turtle(shape='turtle')
    t.color(colors[i])
    t.pu()
    t.goto(x= -230,y= -50 + (i * 30))
    turtles.append(t) 

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won!! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()