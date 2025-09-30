class Calculator:
    def __init__(self, battery : int, batteryMax : int, display : int):
        self.battery : int = battery
        self.batteryMax : int = batteryMax
        self.display : int = display
    def __str__(self) -> str:
        return f"{self.display.2f} : {self.battery}"
def main():

main()