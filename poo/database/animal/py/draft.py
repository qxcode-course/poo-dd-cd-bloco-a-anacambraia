class Animal: 
    def __init__(self, species : str, sound : str): 
        self.species : str = species 
        self.sound : str = sound
        self.age : int = 0

    def ageBy(self, amount: int) -> None:
        self.age += amount
        if self.age > self.ageBy():
            print("warning:" + {species} + "morreu") 
            self.age = self.ageBy()

    def grow(self) -> str:
        if self.age == "grow 1":
            return 10
        if self.age == "M":
            return 20
        if self.age == "G":
            return 30
        return 0
    
    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"

def main():
    animal: Animal = Animal ("", "")
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args [0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal (species, sound)
        elif args[0] == "show":
            print(animal)
        else:
            print("fail:comando invalido")
main()