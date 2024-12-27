from Enemy import *

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
zombie.attack()
