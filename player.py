from turtle import Turtle
FORWARD_DISTANCE = 10
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color('green')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(FORWARD_DISTANCE)

    def at_finish_ine(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def start_again(self):
        self.goto(STARTING_POSITION)


