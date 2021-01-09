class Character:
    def __init__(self):
        self.life = 100
        self.attack_point = 10
    def attack(self, target):
        pass
    def get_hit(self, damage):
        self.life -= damage
class Cratos:
    def __init__(self):
        self.life = 100
        self.damage = 10
        self.attack_point = 10
        self.experience = 0
    def gain_XP(self, amount):
        old_experience = self.experience
        self.experience += amount
        if (self.experience - (old_experience // 10 *10))  // 10 > 0:
            self.damage += (self.experience - (old_experience // 10 *10)) // 10
            self.attack_point += (self.experience - (old_experience // 10 *10))  // 10
            self.experience -= (self.experience - (old_experience // 10 *10))  // 10 * 10
    def attack(self, target):
        target.get_hit(self.attack_point)
    def get_hit(self, damage):
        self.life -= damage
class Drauf:
    def __init__(self, life, damage):
        self.attack_point = damage
        self.life = life
        self.damage = damage
    def get_hit(self, damage):
        self.life -= damage
    def attack(self, enemy):
        enemy.get_hit(self.attack_point)
