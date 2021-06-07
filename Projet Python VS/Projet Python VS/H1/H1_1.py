from PlayerH1_1 import Player

P1 = Player("Warrior")
P2 = Player("Mage")

P1.Damage(30)

print("P1 a",P1.Pv,"points de vie")
print("P2 a",P2.Pv,"points de vie")


def Fight(Player1,Player2):
    while Player1.Pv>0 and Player2.Pv>0:
        Player1.Fight_turn()
        Player2.Fight_turn()