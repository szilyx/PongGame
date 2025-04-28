from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,posx,posy):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(posx, posy)

    def moveup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def movedown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)