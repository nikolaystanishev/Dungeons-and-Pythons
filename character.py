class Character:

    def __init__(self, health, mana):
        self.health_max = health
        self.health = health
        self.mana = mana

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def can_cast(self):
        if self.mana > 0:
            return True
        else:
            return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if self.health + healing_points <= self.healing_points:
            self.health += healing_points
            return True
        else:
            return False

    def take_mana(self, mana_points):
        self.mana += mana_points

    def take_damage(self, damage_points):
        self.health -= damage_points
