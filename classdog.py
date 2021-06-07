from Player import Player
from Dog import Dog

Chien1 = Dog("Rex",5,["Michel","Loïc"])
Chien2 = Dog("Fifi",15,["Micheline"])
Chien3 = Dog("Bibi",1,[])


Chien1.learn("Faire le beau")
Chien2.learn("Faire le beau")

Chien1.learn("Donner la patte")
Chien3.learn("Donner la patte")

Chien2.learn("Faire une roulade")
Chien3.learn("Faire une roulade")

Chien1.tricks_compare(Chien2)
Chien2.tricks_compare(Chien3)