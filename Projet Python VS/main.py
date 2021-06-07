from Dog import Dog

Dog0 = Dog("fien",2,["Martine"])
Dog1 = Dog("Rex",5,["Loic","Bob"])
Dog2 = Dog("toutou",15,["germaine"])

print("chien 1 :",Dog1.name)
print("chien 2 :",Dog2.name)

Dog1.learn("Donner la patte")
Dog2.learn("Donner la patte")

Dog1.learn("Faire le beau")
Dog2.learn("Faire le beau")

Dog1.learn("Faire le mort")

Dog1.compare(Dog2)