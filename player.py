from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
# SLIDE_X = 50


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 10
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def go_up(self):
        self.forward(self.move_speed)

    # def go_left(self):
    #     self.goto((self.xcor() - SLIDE_X), self.ycor())

    # def go_right(self):
    #     self.goto((self.xcor() + SLIDE_X), self.ycor())

    def increase_speed(self):
        self.move_speed += 3
