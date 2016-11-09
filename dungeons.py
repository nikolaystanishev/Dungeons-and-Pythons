from fight import Fight
from random import randint


class Dungeon:

    def __init__(self, file_path):
        self.get_map(file_path)

    def set_enemies(self):
        self.enemies = []
        self.enemies.append(Enemy(health=100, mana=100, damage=20))
        self.enemies.append(Enemy(health=80, mana=80, damage=10))
        self.enemies.append(Enemy(health=150, mana=150, damage=25))
        self.enemies.append(Enemy(health=120, mana=120, damage=15))
        self.enemies.append(Enemy(health=50, mana=70, damage=45))

    def set_treasure(self):
        self.treasure = []
        spell = []
        spell.append(Spell(name="djsn", damage=20, mana_cost=20, cast_range=1))
        spell.append(Spell(name="dksm", damage=10, mana_cost=10, cast_range=3))
        spell.append(Spell(name="sajj", damage=25, mana_cost=25, cast_range=1))
        spell.append(Spell(name="sajk", damage=15, mana_cost=15, cast_range=2))
        spell.append(Spell(name="sakm", damage=45, mana_cost=45, cast_range=1))
        weapon = []
        weapon.append(Weapon(name="snsankansn", damage=20))
        weapon.append(Weapon(name="nsknaknska", damage=10))
        weapon.append(Weapon(name="sanjnkjsna", damage=25))
        weapon.append(Weapon(name="lakklaksla", damage=15))
        weapon.append(Weapon(name="klaskamkml", damage=45))
        self.treasure.append(spell)
        self.treasure.append(weapon)

    def get_map(self, file_path):
        self.dungeon = []
        f = open(file_path, "r")
        for line in f:
            temp = []
            for el in line:
                temp.append(el)
            self.dungeon.append(temp)

    def print_map(self):
        for row in self.dungeon:
            for el in row:
                print(el, end="")

    def spawn(self, hero):
        self.hero = hero
        for y in range(len(self.dungeon)):
            for x in range(len(self.dungeon[y])):
                if self.dungeon[y][x] == "S":
                    self.dungeon[y][x] = "H"
                    return True
        return False

    def get_hero_location(self):
        for y in range(len(self.dungeon)):
            for x in range(len(self.dungeon[y])):
                if self.dungeon[y][x] == "H":
                    return (x, y)
        return False

    def move_up(self):
        location = self.get_hero_location()
        if location[1] < 0:
            return False
        elif self.dungeon[location[0]][location[1]+1] == "#":
            return False
        elif self.dungeon[location[0]][location[1]+1] == "T":
            self.pick_treasure()
        elif self.dungeon[location[0]][location[1]+1] == ".":
            self.dungeon[location[0]][location[1]] = "."
            self.dungeon[location[0]][location[1]+1] = "H"
        elif self.dungeon[location[0]][location[1]+1] == "E":
            self.fight = Fight(self.hero, self.enemies[randint(0, 4)])
            self.fight.start(self)
            if self.fight.start(self):
                self.dungeon[location[0]][location[1]+1] = "H"
            else:
                self.spawn(hero)

    def move_down(self):
        location = self.get_hero_location()
        if location[1] >= len(self.dungeon):
            return False
        elif self.dungeon[location[0]][location[1]-1] == "#":
            return False
        elif self.dungeon[location[0]][location[1]-1] == "T":
            self.pick_treasure()
        elif self.dungeon[location[0]][location[1]-1] == ".":
            self.dungeon[location[0]][location[1]] = "."
            self.dungeon[location[0]][location[1]-1] = "H"
        elif self.dungeon[location[0]][location[1]-1] == "E":
            self.fight = Fight(self.hero, self.enemies[randint(0, 4)])
            if self.fight.start(self):
                self.dungeon[location[0]][location[1]-1] = "H"
            else:
                self.spawn(hero)

    def move_left(self):
        location = self.get_hero_location()
        if location[0] < 0:
            return False
        elif self.dungeon[location[0]-1][location[1]] == "#":
            return False
        elif self.dungeon[location[0]-1][location[1]] == "T":
            self.pick_treasure()
        elif self.dungeon[location[0]-1][location[1]] == ".":
            self.dungeon[location[0]][location[1]] = "."
            self.dungeon[location[0]-1][location[1]] = "H"
        elif self.dungeon[location[0]-1][location[1]] == "E":
            self.fight = Fight(self.hero, self.enemies[randint(0, 4)])
            self.fight.start(self)
            if self.fight.start(self):
                self.dungeon[location[0]-1][location[1]] = "H"
            else:
                self.spawn(hero)

    def move_right(self):
        location = self.get_hero_location()
        if location[0] >= len(self.dungeon[0])-1:
            return False
        elif self.dungeon[location[0]+1][location[1]] == "#":
            return False
        elif self.dungeon[location[0]+1][location[1]] == "T":
            self.pick_treasure()
        elif self.dungeon[location[0]+1][location[1]] == ".":
            self.dungeon[location[0]][location[1]] = "."
            self.dungeon[location[0]+1][location[1]] = "H"
        elif self.dungeon[location[0]+1][location[1]] == "E":
            self.fight = Fight(self.hero, self.enemies[randint(0, 4)])
            if self.fight.start(self):
                self.dungeon[location[0]+1][location[1]] = "H"
            else:
                self.spawn(hero)

    def move_hero(self, direction):
        if direction == "up":
            self.move_up()
        elif direction == "down":
            self.move_down()
        elif direction == "left":
            self.move_left()
        elif direction == "right":
            self.move_right()

    def pick_treasure(self):
        index = randint(0, 1)
        if index:
            self.hero.equip(self.pick_treasures[1][randint(0, 4)])
        else:
            self.hero.learn(self.pick_treasures[0][randint(0, 4)])

map1 = Dungeon("level1.txt")
map1.print_map()
