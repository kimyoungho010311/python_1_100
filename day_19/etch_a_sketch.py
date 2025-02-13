from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwars():
    tim.backward(10)

def counter_clokwise():
    tim.left(10)

def clokwise():
    tim.right(10)

def clear_drawing():
    tim.pu()
    tim.clear()
    tim.home()
    tim.pd()
    
screen.listen()
screen.onkey(move_forwards,'w')
screen.onkey(move_backwars, 's')
screen.onkey(counter_clokwise, 'a')
screen.onkey(clokwise, "d")
screen.onkey(clear_drawing, 'c')
screen.exitonclick()