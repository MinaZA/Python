class Player:

    def __str__(self):
        result = self.role + str(self.pv) + str(self.Str) + str(self.Def)
        return result

    def __init__(self,role):
        self.role = role
        self.inventory = []
        if role == "Warrior":
            self.pv = 20
            self.Str = 5
            self.Def = 10
        elif role == "Mage":
            self.pv = 10
            self.Str = 10
            self.Def = 5

    def Damage(self,dmg):
        dmg = dmg - self.Def
        self.pv -= dmg

    def Open_inventory(self):
        for item in self.inventory:
            print(item)