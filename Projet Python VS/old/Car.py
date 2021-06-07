class Car:
    id = 123 #Variable partagée par toutes les instances Variable de classe

    def __init__(self, km):
        self.name = "ma voiture" #Variable d'instance 
        self.km = km
        self.targets = []

    def AddTarget(self, target):
        self.targets.append(target) 

    def printHello(self):
        print('hello world')