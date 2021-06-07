class Player:

    def __init__(self,role):
        if role == "Warrior":
            self.Atk = 10
            self.Def = 3
            self.Pv = 100
        elif role == "Mage":
            self.Atk = 30
            self.Def = 2
            self.Pv = 50
        
    def Damage(self, dmg):
        dmg = dmg - self.Def
        self.Pv = self.Pv - dmg
        
