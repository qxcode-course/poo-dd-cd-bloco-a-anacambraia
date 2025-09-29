class Animal: 
    def __init__(self, species : str, sound : str): 
        self.species : str = species 
        self.sound : str = sound
        self.age : int = 0

    def ageBy(self, increment: int):
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            return
        self.age += increment
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")
   
    def makeSound(self) -> str:
        if self.age == 0:
            return "---"
        elif self.age == 4:
            return "RIP"
        else:
            return self.sound

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
        elif args[0] == "grow":
            amount: int = int(args[1])
            animal.ageBy(amount)
        elif args[0] == "noise":
            print(animal.makeSound())
        else:
            print("fail:comando invalido")
main()