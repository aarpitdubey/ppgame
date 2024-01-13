from turtle import Screen, Turtle # Screen module
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Step 1: Create a Screen.
screen = Screen() # Screen object
screen.bgcolor("black") #
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # Turn off the animation


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()
# m_paddle = Paddle((100, 100))

# Step 2: Creating a Paddle
paddle = Turtle() # Paddle object

# Adding event listner
screen.listen()
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    
    # Detect collision with wall
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
        
    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        
    # detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    # detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()