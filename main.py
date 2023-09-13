from turtle import Turtle, Screen
from turtleTim import TurtleTim
from enemies import Enemies
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = TurtleTim()
screen.listen()
screen.onkeypress(tim.up, "w")
screen.onkeypress(tim.down, "s")
screen.onkeypress(tim.right, "d")
screen.onkeypress(tim.left, "a")


score = Scoreboard()
enemy = Enemies()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    enemy.enemy_create()
    enemy.move_enemies()

    for en in enemy.enemies:
        if tim.distance(en) < 20:
            game_is_on = False
            score.game_over()

    if tim.ycor() > 280:
        score.level_up()
        tim.level_up()
        enemy.level_up()

screen.exitonclick()