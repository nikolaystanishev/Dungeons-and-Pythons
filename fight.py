from hero import Hero
from enemy import Enemy


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy


def start(self, dungeon):
    while self.hero.is_alive() and self.enemy.is_alive():
        hero = self.hero.__dict__()
        spell_or_weapon = 'weapon'
        if weapon in hero and spell in hero:
            if hero[weapon][damage] == hero[spell][damage]:
                spell_or_weapon = 'spell'
        elif spell in hero:
            spell_or_weapon = 'spell'
        hero.attack(by=spell_or_weapon)
        hero.mana -= hero.spell.mana_cost
        self.hero.take_damage(self.enemy.damage)
        self.enemy.take_damage(self.hero.)
    self.stop()


def stop(self):
    print("Game over!")
    print(exit())
