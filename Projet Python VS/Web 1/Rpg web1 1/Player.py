from Attaque import Attaque

class Player:

    def __str__(self):
        result = self.role + str(self.pv) + str(self.Str) + str(self.Def)
        return result

    def __init__(self,role):
        self.role = role
        self.inventory = []
        self.list_attaque = []
        if role == "Warrior":
            self.pv = 20
            self.Str = 5
            self.Def = 10
            Atk = Attaque("Coup de poing",90,2)
            self.list_attaque.append(Atk)
        elif role == "Mage":
            self.pv = 10
            self.Str = 10
            self.Def = 5
            self.list_attaque.append(Attaque("Boule de feu",50,5))


    def Damage(self,dmg):
        dmg = dmg - self.Def
        self.pv -= dmg

    def Open_inventory(self):
        for item in self.inventory:
            print(item)

    def Drink_potion(self,potion):
        if potion.Type == "heal":
            self.pv += potion.power
        elif potion.Type == "Force":
            self.Str += potion.power
        elif potion.Type == "Defense":
            self.Def += potion.power

    