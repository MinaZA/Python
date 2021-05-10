from Joueur import Joueur
from Mot import Mot
from Phrase import Phrase

class GAME :

    def __init__(self) :
        self.joueur1 = Joueur("Francis")
        self.joueur2 = Joueur("Maurice")
        self.Combat()


    def Combat(self) :
        x = 0
        print(self.joueur1.name + "VS" + self.joueur2.name)
        while(self.joueur1.pv > 0 and self.joueur2.pv > 0):
            print(self.joueur1)
            print(self.joueur2)
    

            print("Que voulez-vous faire ?")
            print("1 - Attaquer ?")
            print("2 - Boire une potion")
            Choice_user = input()

            if Choice_user == "1" :
                x = x + 1
                Motpropose = Mot(str(x))
                Phrasepropose = Phrase(str(x))
                print(Phrasepropose.phrase)
                i=0
                j=1
                while(i<len(Motpropose.liste_mot)):
                    proposition = ""
                    proposition = str(j) + ") -- " + Motpropose.liste_mot[int(i)] + " --"
                    print(proposition)
                    j = j + 1
                    i = i + 1
                
                print("Veuillez choisir votre arme !")
                Choice_user = input()
                reponse = ""
                if Choice_user == "1" :
                    reponse = Phrasepropose.phrase + Motpropose.liste_mot[0]
                    print(reponse)
                if Choice_user == "2" :
                    reponse = Phrasepropose.phrase + Motpropose.liste_mot[1]
                    print(reponse)
                if Choice_user == "3" :
                    reponse = Phrasepropose.phrase + Motpropose.liste_mot[2]
                    print(reponse)

        
