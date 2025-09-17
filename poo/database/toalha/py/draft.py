class Towel: 
    def __init__(self, color : str, size : str): #construir meu obejto e definir atributos
        self.color : str = 'red' #atributos
        self.size : str = 'p'
        self.wetness : int = '0' 

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0