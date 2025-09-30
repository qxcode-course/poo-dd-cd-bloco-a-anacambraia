class Car:
    def __init__(self, gas, gasMax, passMax):
        self.passa = 0
        self.Km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100 

    def enter(self):
        if self.passa >= self.passMax:
            print("fail: limite de pessoas atingido")
        else:
            self.passa += 1

    def leave(self):
        if self.passa <= 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.passa -= 1

    def drive(self, distance):
        if self.passa == 0:
            print("fail: não há ninguém no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if self.gas >= distance:
            self.km += distance
            self.gas -= distance
        else:
            distance = self.gas
            self.km += distance
            self.gas = 0
            print(f"fail: tanque vazio após andar {distance} km.")

    def fuel(self, amount) -> int:
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax
            return
            self.gas += amount
        
    def __str__(self) -> str:
        return f"pass: {self.passa}, gas: {self.gas}, km: {self.Km}"

def main():
    carro = Car ("", "", "")
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            carro.fuel()
main()