from PythonRefresher.OOPS.Classes.Enemy import Enemy

class Orge(Enemy):

    def __init__(self, health_points=60, attack_damage=4, special_attack_damage = 10):

        # calling super class constructor
        super().__init__(
            enemy_type = "Orge",
            health_points = health_points,
            attack_damage = attack_damage,
            special_attack_damage = special_attack_damage
        )

    def talk(self):
        print("Beating hands on the ground.")