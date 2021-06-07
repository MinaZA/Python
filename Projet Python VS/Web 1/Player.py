class Player:

    Inventory = []


    def __init__(self,role):
        if role == "Warrior":
            self.Pv = 20
            self.Str = 5
            self.Def = 10
        elif role == "Mage":
            self.Pv = 10
            self.Str = 10
            self.Def = 5

    def Damage(self,dmg):
        dmg = dmg - self.Def
        self.pv -= dmg

    def print_inventory(self):
        for item in self.Inventory:
            print(item)
