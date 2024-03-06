from character import Hero, Enemy
from weapon import Weapon
import os

#setup
healing_staff = Weapon("Healing Staff","healing", -3,5)
empty_handed = Weapon("Nothing", "None", 0, 0)

protagonist = Hero("Protagonist", 100)
protagonist.health_max = 100
ally = Enemy("Ally", 100, healing_staff)

protagonist.equip(empty_handed)
protagonist.health = 10

#main game loop
while True:
    os.system("clear")

    protagonist.attack(ally)
    ally.attack(protagonist)

    protagonist.health_bar.draw()
    ally.health_bar.draw()

    input()