from random import random

from Enemy import *
from PythonRefresher.OOPS.Classes.Orge import Orge
from PythonRefresher.OOPS.Classes.Zombie import Zombie

"""
Before constructor
"""

# zombie = Enemy()
# zombie.enemy_type = "Zombie"
# print(f"{zombie.enemy_type} has health of {zombie.health_points} and can do a damage of {zombie.attack_damage}")

"""
After constructor
"""

zombie = Enemy("Zombie")

zombie.talk()
zombie.walk_forward()
# zombie.attack()

# zombie.__enemy_type = "Orge" # this line adds new variable in the object
# print(zombie.__enemy_type)
#
# zombie.talk()
#
# print(zombie.get_type_of_enemy())
#
# zombie_1 = Zombie()
#
# zombie_1.talk()
# zombie_1.walk_forward()
# zombie_1.attack()
#
# def battle(e : Enemy):
#     e.talk()
#     e.attack()
#
# battle(zombie)
# battle(zombie_1)
#
# enemy : Enemy = Zombie(health_points=50, attack_damage=5)
# battle(enemy)

# Game logic

def fight(e1 : Enemy, e2 : Enemy):
    e1.talk()
    e2.talk()

    gladiators = [e1, e2]

    while e1.health_points > 0 and e2.health_points > 0:
        e1.take_damage(e2.attack_damage)
        e2.take_damage(e1.attack_damage)
        print(f"Health of 1: {e1.health_points}, Health of 2: {e2.health_points}")
        e1.take_damage(e2.special_attack_damage)
        e2.take_damage(e1.special_attack_damage)
        print(f"Health of 1: {e1.health_points}, Health of 2: {e2.health_points}")

    if e1.health_points <= 0:
        print(f"{e2.get_type_of_enemy()} wins the battle!")
    else: print(f"{e1.get_type_of_enemy()} wins the battle!")

zombie_enemy = Zombie(health_points=100)
orge_enemy = Orge()

fight(zombie_enemy, orge_enemy)