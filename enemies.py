from turtle import Turtle
import random
from scoreboard import Scoreboard

COLORS = ["red", "green", "orange", "yellow", "blue", "purple", "pink"]

class Enemies():
    def __init__(self):
        self.enemies = []
        self.speed = 5
        self.random_quan = 7

    def enemy_create(self):
        random_chance = random.randint(1, self.random_quan)
        if random_chance == 3:
            new_enemy = Turtle("square")
            new_enemy.shapesize(stretch_wid=1, stretch_len=2)
            new_enemy.penup()
            new_enemy.color(random.choice(COLORS))
            new_enemy.setheading(180)
            random_y = random.randint(-230, 230)
            new_enemy.goto(300, random_y)
            self.enemies.append(new_enemy)

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.forward(self.speed)

    def level_up(self):
        self.random_quan = random.randint(4, 7)
        self.speed += 2
