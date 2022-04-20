import time
from turtle import Screen
from player import Player
from car_manager import CarManagerw
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing - Replit Style")
screen.tracer(0)

def increase_all():
    scoreboard.increase_level()
    cars.increase_speed()
    player.increase_speed()


player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "w")
# screen.onkeypress(player.go_left, "a")
# screen.onkeypress(player.go_right, "d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.goto(0, -280)
        increase_all()


screen.exitonclick()
