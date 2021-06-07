#from monster import *
#test()

print("Bonjour mon brave guerrier, es-tu prêt pour l'aventure !?")
print
a = str (input())
MDP ="oui"

while a != MDP:
      print("Recommences petit insolant")
      print("Tu connais très bien la réponse ")
      a = str (input())
else:
  print("AH, parfait on commence alors.")
  print("Ecris ton Nom et Prénom")
  Name =str (input())

def Menu():
  print("1: Create new game")
  print("2: Load Game")
  print("3: About")
  print("4: Exit")
  Choix = int(input())
  if Choix == 1:
    PlayGame()
  elif Choix == 2:
    LoadGame()
  elif Choix == 3:
    About()
  else:
    Exit()

def PlayGame():
  print(Name," Lancer le jeu ")
  TargetMovement = Movement()
  TargetMaps = Maps()
  Event(TargetMovement, TargetMaps)

def LoadGame():
  print("TODO LoadGame")
  PlayGame()

def About():
  print("TODO about")
  Menu()

def Exit():
  print("TODO exit")

def Description(Lieu):
  if Lieu == 1 :
    print("Ah... la montagne, avec ces terres arides, et des créatures aussi bizarres")
    print("les unes que les autres. Et sa majesté le Roi Phénix perché au plus haut sommet de la montagne.")
  if Lieu == 2 :
    print("Ah... la mer, l'endroit parfait pour des vacances, mais attention aux requins et sa majesté le Kraken. ")
  if Lieu == 3 :
    print("Ah... la forêt, l'endroit parfait pour des picnics entres amis, mais attention") 
    print("au loup, à leur cri sombre aini qu'à sa majesté l'Ours. ")
  if Lieu == 4 :
    print("Ah... la ville, l'endroit parfait pour des touristes, mais attention aux Chauve-souris, ") 
    print("assoifées de sang, sans oublier sa majesté le Vampire. ")

  return Lieu

def Movement():
  print("Faire le déplacement du player", Name)
  print("1: En montagne")
  print("2: En mer")
  print("3: En forêt")
  print("4: En ville")
  Lieu = int (input())
  if Lieu == 1:
    print("C'est parti pour la montagne !")
    Description(Lieu) 
  elif Lieu == 2:
    print("c'est parti pour la mer !")
    Description(Lieu)
  elif Lieu == 3:
    print("c'est parti pour la forêt !")
    Description(Lieu)
  elif Lieu == 4:
    print("c'est parti pour la ville !")
    Description(Lieu)
  
  return Lieu

def Event(Lieu, maps):
  print(Name,"explore les environts avec 20 PV")
  #Maps()
  Combat()
  Item()

def Maps():
  print(Name,"choisie son chemin")
  print("1: Monter")
  print("2: Decendre")
  print("3: Avancer")
  print("4: Reculer")
  choix = int (input())
  maps = [[0, 1, 0, 2,] , [2, 1, 0, 0,] , [2, 1, 0, 1,] , [0, 2, 0, 2,] , [1, 0, 1, 3,]]
  x = 0
  y = 0


  if choix == 1:
    print(Name,"monter")
    choixchemin(choix, maps, y, x)
  elif choix == 2:
    print(Name,"decendre")
    choixchemin(choix, maps, y, x)
  elif choix == 3:
    print(Name,"avancer")
    choixchemin(choix, maps, y, x)
  elif choix == 4:
    print(Name,"reculer")
    choixchemin(choix, maps, y, x)
  i = 0
  while i < len(maps) :
    print(maps[i])
    i = i + 1
  return choix, y, x

def choixchemin(choix, maps, y ,x) :
  
  if choix == 1 :
    y = y - 1
    if y < 0 :
      y = 0
      print("impossible de monter")
    chiffremaps(maps,y,x)
    maps[y][x] = "P"
  if choix == 2 :
    y = y + 1
    if y > 4 :
      y = 4
      print("impossible de decendre")
    chiffremaps(maps,y,x)
    maps[y][x] = "P"
  if choix == 3 :
    x = x + 1
    if x > 3 :
      x = 3
      print("impossible d'avancé")
    chiffremaps(maps,y,x)
    maps[y][x] = "P"
  if choix == 4 :
    x = x - 1
    if x < 0 :
      x = 0
      print("impossible de reculé")
    chiffremaps(maps,y,x)
    maps[y][x] = "P"

  return choix,maps,y,x

def chiffremaps(maps,y,x) :
  if maps[y][x] == 0 :
    print(Name,"ne vois rien aux alentour")
    Maps()
  if maps[y][x] == 1 :
    print(Name, "rencontre un commerçant")
    Maps()
  if maps[y][x] == 2 :
    print(Name, "rencontre un monstre")
    Combat()
  if maps[y][x] == 3 :
    print(Name, "rencontre le chef des monstres")
    Combat()
  return(maps,y,x)

def Combat():
  print( Name,"Combat")

def Item():
  print(Name, "Item")


Menu()