from character import Character
from weapon import Weapon


class Hero(Charcter):
    def __init__(self, applyname, title, mana_regeneration_rate):
        super().__init__(healt, mana)
        self.applyname = applyname
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def know_us(self):
        return "{} the {}".format(self.applyname, self.title)

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(by):
        if by == 'spell':
            return self.spell.damage
        else:
            return self.weapon.damage
