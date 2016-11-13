class Message:
    def __init__(hero, enemy, dungeon):
        self.hero = hero
        self.enemy = enemy
        self.dungeon = dungeon

    def start_fight(self):
        return "A fight is started between our Hero(health={0}, mana={1}) and Enemey(health={2}, mana={3}, damage={4})\
        ".format(self.hero.health, self.hero.mana, self.enemy.health, self.enemy.mana, self.enemy.damage)

    def hero_cast(self):
        return "Hero casts a {0}, hits enemy for {1} dmg.Enemy health is {2} \
        ".format(self.hero.spell.name, self.hero.spell.damage, self.enemy.get_health())

    def no_more_mana(self):
        return "Hero does not have mana for another {0}.".format(self.hero.spell.name)

    def hero_hit(self):
        return "Hero hits with {0} for {1} dmg. Enemy health is {2}".format(self.hero.weapon.name, self.hero.weapon.damage, self.enemy.get_health())

    def enemy_hit(self):
        return "Enemy hits hero with {0}dmg. Hero health is {1}".format(self.enemy.damage, self.hero.get_health())

    def is_dead(self, dead):
        return "{0} is dead!".format(dead)
