from character import Character


class Enemies(Character):
    def __init__(self, health, mana, demage):
        super().__init__(health, mana)
        self.damege = demage

    def attack():
        return self.damege
