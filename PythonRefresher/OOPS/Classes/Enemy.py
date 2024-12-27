class Enemy:
    # enemy_type : str
    # health_points : int = 30
    # attack_damage : int = 1

    # non parameterized constructor
    # def __init__(self):
    #     print("Creating the new enemy.")

    # parameterized constructor
    def __init__(self, enemy_type, health_points=30, attack_damage=1):
        self.enemy_type = enemy_type
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.enemy_type} run for your life.")

    def walk_forward(self):
        print(f"{self.enemy_type} is moving closer to you.")

    def attack(self):
        print(f"{self.enemy_type} is attacking, causing the damage of {self.attack_damage}.")