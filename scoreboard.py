from turtle import Turtle
FONT = ('Courier', 24, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.level = 1
        self.goto(-280, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.color('white')
        self.write(f"LEVEL: {self.level}", align='left', font=('Courier', 15, 'normal'))

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.penup()
        self.color('white')
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)


