class Potion:
    def __str__(self):
        return "C'est une potion de "+self.Type+" de puissance "+str(self.power)

    def __init__(self,Type,power):
        self.Type = Type
        self.power = power

    