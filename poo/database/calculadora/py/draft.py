class Calculator:
    def __init__(self, batteryMax : int):
        self.battery : int = 0
        self.batteryMax : int = batteryMax
        self.display : float = 0.0

    def charge(self, value):
        self.battery += value
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a : int, b : int):
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return
        self.battery -= 1
        self.display = a + b

    def division(self, num : int, den : int):
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return
        self.battery -= 1
        if den == 0:
            print("fail: divisao por zero")
            return
        self.display = num / den
        

    
    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
def main():
    calculadora = Calculator ("")
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            calculadora = Calculator(int(args[1]))
        elif args[0] == "show":
            print(calculadora)
        elif args[0] == "charge":
            calculadora.charge(int(args[1]))
        elif args[0] == "sum":
            calculadora.sum(int(args[1]), int(args[2]))
        elif args[0] == "div":
            calculadora.division(int(args[1]), int(args[2]))

    
main()