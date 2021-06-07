class Player:

    def __init__(self,role):
        if role == "Warrior":
            self.pv = 100
            self.attaque = 10
            self.defense = 5
        elif role == "Mage":
            self.pv = 50
            self.attaque = 25
            self.defense = 3
        
    def Damage(self, dmg):
        dmg = dmg - self.defense
        self.pv = self.pv - dmg
        