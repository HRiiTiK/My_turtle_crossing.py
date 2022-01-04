from turtle import Turtle
import random
COLORS = ['red', 'yellow', 'pink', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car_making = random.randint(1, 6)  # when 1 comes then n then only a car will create
        if car_making == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250, 240)
            new_car.goto(300, random_y)
            self.cars_list.append(new_car)

    def move(self):
        for car in self.cars_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
