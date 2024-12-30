from PythonRefresher.OOPS.Classes.Enemy import Enemy


class Zombie(Enemy):

    def __init__(self, health_points=10, attack_damage=2, special_attack_damage = 5):

        # calling super class constructor
        super().__init__(
            enemy_type = "Zombie",
            health_points = health_points,
            attack_damage = attack_damage,
            special_attack_damage = special_attack_damage
        )

    def talk(self):
        print("Grrrrhhhhh....")
