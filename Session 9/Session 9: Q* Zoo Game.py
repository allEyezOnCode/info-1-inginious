class Animal:
    def __init__(self, name):
        self.name = name
        self.diurnal = None
        self.nb_legs = None
        self.asleep = False
    def sleep(self):
        if self.asleep == True: raise RuntimeError
        self.asleep = True
    def wake_up(self):
        if self.asleep == False: raise RuntimeError
        self.asleep = False
        
class Lion(Animal):
    def __init__(self, name):
        self.name = name
        self.diurnal = True
        self.nb_legs = 4
        self.asleep = False
    def roar(self):
        print("ROARRR!!!")
class Owl(Animal):
    def __init__(self, name):
        self.name = name
        self.diurnal = False
        self.nb_legs = 2
        self.asleep = False
    def fly(self):
        pass
class Giraffe(Animal):
    def __init__(self, name, neck_length):
        self.name = name
        self.diurnal = True
        self.nb_legs = 4
        self.asleep = False
        if (type(neck_length) != int and type(neck_length) != float) or neck_length < 0: raise ValueError
        self.neck_length = neck_length
class Zoo:
    def __init__(self):
        self.animals = []
    def add_animal(self, animal):
        if type(animal) not in [Lion, Owl, Giraffe, Animal]: raise ValueError
        self.animals.append(animal)
def create_my_zoo():
    zoo = Zoo()
    zoo.add_animal(Lion("a"))
    zoo.add_animal(Owl("d"))
    zoo.add_animal(Giraffe("dfd", 25))
    zoo.add_animal(Giraffe("cfddjf", 15))
    return zoo
        
