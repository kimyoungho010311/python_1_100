from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#TODO : 화면의 아래쪽에서부터 출발하는 거북이를 만들어 “위” 키가 입력되면 북쪽으로 움직이세요. 컷 



class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.goto(STARTING_POSITION)
        self.left(90)
        
    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        pass