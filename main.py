from turtle import Turtle, Screen
from paddle import Paddle

MainScreen = Screen()
MainScreen.setup(width= 800, height=600)
MainScreen.bgcolor("black")
MainScreen.title("Pong Game")

MainScreen.tracer(0)

MainScreen.listen()

paddle_1 = Paddle(350,0)
paddle_2 = Paddle(-350,0)
MainScreen.onkey(paddle_1.moveup, "Up")
MainScreen.onkey(paddle_1.movedown, "Down")
MainScreen.onkey(paddle_2.moveup, "w")
MainScreen.onkey(paddle_2.movedown, "s")
game_is_on = True

while game_is_on:
    MainScreen.update()
MainScreen.exitonclick()