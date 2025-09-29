class Car:
    def __init__(self, passa : int, passMax : int, gas : int, gasMax : int, Km : int):
        self.passa : int = passa
        self.passMax : int = passMax
        self.gas : int = gas
        self.gasMax : int = gasMax
        self.Km : int = Km

    
    def __str__(self) -> str:
        return f"{self.passa}:{self.gas}:{self.Km}"

def main():
    carro = Car ("", "")
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
main()