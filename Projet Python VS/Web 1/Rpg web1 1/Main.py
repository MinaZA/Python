from Player import Player
from Potion import Potion



P = Player("Warrior")

P.inventory.append(Potion("heal",10))
P.inventory.append(Potion("Force",5))

P.Open_inventory()

print(P.pv)
P.Drink_potion(P.inventory[0])
print(P.pv)
