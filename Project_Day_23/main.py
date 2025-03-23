import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.go_up, "Up")

cars = CarManager()
cars.create_cars()

score_board = Scoreboard()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    #detect collision with the car...
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    #detect successful crossing...
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        score_board.level_up()


screen.exitonclick()
