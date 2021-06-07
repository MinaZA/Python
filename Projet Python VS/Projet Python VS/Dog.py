
class Dog:
    def __init__(self,name,age,owners):
        self.name = name
        self.age = age
        self.owners = owners
        self.tricks = [] 

    def learn(self,trick):
        self.tricks.append(trick)

    def compare(self,dog):
        i = 0
        while i < len(self.tricks):
            if self.tricks[i] in dog.tricks:
                print(self.tricks[i])
            i+=1
        
