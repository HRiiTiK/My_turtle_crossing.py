from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Score()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars_list:
        if player.distance(car) <= 30:
            scoreboard.game_over()
            game_is_on = False

    if player.at_finish_ine():
        player.start_again()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_level()


screen.exitonclick()