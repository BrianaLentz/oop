
# Parent class
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet('Cooper', pet, ['sit','shake'], 100, 50)
        


    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self
    
# child class
class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self. energy = energy
        

    def sleep(self):
        self.energy += 25
        print()
        return self

    def eat(self):
        self.energy += 5
        self.health +=10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("Bark! Bark! Bark!")
        return self


Zach = Ninja('Zach', 'Lentz', 'Biscuits', 'kibble', 'dog')

print(f"{Zach.pet.name}")
print(f"{Zach.pet.health}")
Zach.walk().feed().bathe()
print(f"{Zach.pet.health}")
print(f"{Zach.pet.energy}")

