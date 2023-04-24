import random

class Ruleta:
    def __init__(self, saldo=50000):
        self.saldo = saldo

    def lanzar(self, cantidad, numero):
        resultado = random.randrange(0, 37)
        if resultado == 0:
            self.saldo += cantidad
        elif resultado != numero:
            self.saldo += cantidad
        else:
            self.saldo -= cantidad * 36
        return resultado
    

class Jugador:
    def __init__(self, saldo=1000):
        self.saldo = saldo
    
    def apostar(self, cantidad, numero, resultado):
        self.saldo -= cantidad
        if resultado == numero and resultado != 0:
            self.saldo += cantidad * 36            
