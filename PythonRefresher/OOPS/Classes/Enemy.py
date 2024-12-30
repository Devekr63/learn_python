class Enemy:
    # enemy_type : str
    # health_points : int = 30
    # attack_damage : int = 1

    # non parameterized constructor
    # def __init__(self):
    #     print("Creating the new enemy.")

    # parameterized constructor
    def __init__(self, enemy_type, health_points=30, attack_damage=1, special_attack_damage = 2):
        # self.enemy_type = enemy_type

        # making a variable private in the class
        self.__enemy_type = enemy_type

        self.health_points = health_points
        self.attack_damage = attack_damage
        self.special_attack_damage = special_attack_damage

    def get_type_of_enemy(self):
        return self.__enemy_type

    def talk(self):
        print(f"I am a {self.__enemy_type} run for your life.")

    def walk_forward(self):
        print(f"{self.__enemy_type} is moving closer to you.")

    def attack(self, enemy):
        print(f"{self.__enemy_type} is attacking, causing the damage of {self.attack_damage}.")
        enemy.take_damage(self.attack_damage)

    def special_attack(self, enemy):
        print("Enemy does not have any special attacks.")
        enemy.take_damage(self.attack_damage)

    def take_damage(self, damage):
        self.health_points -= damage