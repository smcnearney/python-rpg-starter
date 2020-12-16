class Character:

    def __init__(self, health, power, hero, herohealth, heropower, goblin, goblinhealth, goblinpower):
        self.health = health
        self.power = power
        hero.health = herohealth
        hero.power = heropower
        goblin.health = goblinhealth
        goblin.power = goblinpower

    
    def alive(self):
        self.health > 0

    def print_status(self):
        print("""
        %s Health: %d
        %s Power: %d
        """ % (self.health, self.power))
        


class Hero(Character):
    
    def attack(self, goblin):
        goblin.health -= self.power
    
    # def print_status(self):
    #     print("""
    #     Hero Health: %d
    #     Hero Power: %d
    #     """ % (self.health, self.power))


class Goblin(Character):

    def attack(self, hero):
        hero.health -= self.power

    # def print_status(self):
    #     print("""
    #     Goblin Health: %d
    #     Goblin Power: %d
    #     """ % (self.health, self.power))

