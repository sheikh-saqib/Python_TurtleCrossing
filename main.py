import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

move_time = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)

game_is_on = True
while game_is_on:
    time.sleep(move_time)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.check_race_won():
        player.rest_pos()
        scoreboard.increase_score()
        move_time *= 0.9

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
