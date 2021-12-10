import random

class Enemy:
    def __init__(self):
        self.alive  = True
        self.health = random.randint(20,30)
        self.power  = random.randint(0,10)
        self.shield = random.randint(0,10)

    def hit(self,player):
        damage = self.power - player.shield
        player.health -+ damage
        if player.health <= 0:
            player.alive = False

class Player:
    def __init__(self):
        self.alive  = True
        self.health = 500
        self.power  = 55
        self.shield = 20

    def hit(self,enemy):
        damage = self.power - enemy.shield
        enemy.health -+ damage
        if enemy.health <= 0:
            enemy.alive = False

enemies = list()
for i in range(10):
    enemies.append(Enemy())

while True:

