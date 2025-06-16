from turtle import Screen
from snake import *
from food import Food
from scoreboard import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        score_board.increase_score()
        food.refresh()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()
    # detect collision with its tail
    # if head meets any of the segments in tail then game is over
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()
