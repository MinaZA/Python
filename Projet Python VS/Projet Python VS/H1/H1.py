from PlayerH1 import Player

P1 = Player("Warrior")

P1.Damage(20)

P2 = Player("Mage")

print("P1:",P1.attaque,P1.defense,P1.pv)
print("P2:",P2.attaque,P2.defense,P2.pv)

def Fight(Player1, Player2):
    while Player1.pv > 0 and Player2.pv > 0:
        Player1.Take_turn()
        Player2.Take_turn()


