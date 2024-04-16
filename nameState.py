from turtle import Turtle

FONT = ("Courier", 12, "normal")


class NameState(Turtle):
    def __init__(self, x, y, state_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.teleport(x, y)
        self.write(state_name, False, 'center', FONT)
