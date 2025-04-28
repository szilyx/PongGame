from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

MainScreen = Screen()
MainScreen.setup(width= 800, height=600)
MainScreen.bgcolor("black")
MainScreen.title("Pong Game")

MainScreen.tracer(0)

MainScreen.listen()

paddle_1 = Paddle(350,0)
paddle_2 = Paddle(-350,0)
scoreboard = Scoreboard()
ball = Ball()
MainScreen.onkey(paddle_1.moveup, "Up")
MainScreen.onkey(paddle_1.movedown, "Down")
MainScreen.onkey(paddle_2.moveup, "w")
MainScreen.onkey(paddle_2.movedown, "s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    MainScreen.update()
    ball.start()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restargame()
        scoreboard.l_score += 1
        scoreboard.refresh_board()

    if ball.xcor() < -380:
        ball.restargame()
        scoreboard.r_score += 1
        scoreboard.refresh_board()

MainScreen.exitonclick()