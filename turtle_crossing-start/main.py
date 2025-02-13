import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'w')
screen.onkey(player.move, 'Up')

counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    #STARTING_POSITION = (0, -280)
    if player.ycor() > 290:
        print("Win")
        player.goto(0, -280)
        car_manager.next_leve()
        scoreboard.increase_level()

        
screen.exitonclick()