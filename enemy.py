from character import Character


class Enemy(Character):
    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self.damage = damage

    def attack(self):
        return self.damage
