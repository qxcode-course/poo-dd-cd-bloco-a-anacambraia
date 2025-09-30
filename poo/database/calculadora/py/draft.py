class Calculator:
    def __init__(self, batteryMax : int):
        self.battery : int = 0
        self.batteryMax : int = batteryMax
        self.display : float = 0.0
    
    def charge(self, value : int) -> None:
        if 


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
main()