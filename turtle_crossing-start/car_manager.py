from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# TODO: 높이 20픽셀, 너비 40픽셀인 자동차들을 y축 범위 내에서 무작위로 생성하고, 화면의 왼쪽 가장자리로 움직이세요.
# 자동차는 화면의 위아래 가장자리에서 50픽셀 이상 띄워서 생성해야 합니다(거북이를 위한 안전지대라고 생각하세요). 
# 힌트) 게임 반복문이 6번 실행될 때마다 자동차를 새로 생성하세요. 풀다가 막히면 4단계 설명 영상을 확인해 보세요.

class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def next_leve(self):
        self.car_speed += MOVE_INCREMENT
        