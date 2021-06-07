class PlayerRpg:

    def __init__(self,role):
        if role == "Warrior":
            self.health = 5
            self.force = 3
            self.defense = 2
        elif role == "Mage":
            self.health = 2
            self.force = 7
            self.defense = 2

    def Damage(self,damage_number):
        self.health -= damage_number - self.defense