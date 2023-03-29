from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super(Paddle, self).__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def up(self):
        ycor = self.ycor() + 30
        self.goto(x=self.xcor(), y=ycor)

    def down(self):
        ycor = self.ycor() - 30
        self.goto(x=self.xcor(), y=ycor)
