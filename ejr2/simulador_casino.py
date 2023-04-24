import random

class Ruleta:
    def __init__(self, saldo=50000, resultado=None):
        self.saldo = saldo
        self.resultado = resultado
    
    def lanzar(self):
        self.resultado = random.randrange(0, 37)

    def numero(self, cantidad, numero):
        if self.resultado == 0:
            self.saldo += cantidad
        elif self.resultado != numero:
            self.saldo += cantidad
        else:
            self.saldo -= cantidad * 36
        return self.resultado
    
    def par(self, cantidad, paridad):
        if self.resultado == 0:
            self.saldo += cantidad
        elif self.resultado%2 != paridad:
            self.saldo += cantidad
        else:
            self.saldo -= cantidad * 2
        return self.resultado
    

class Jugador:
    def __init__(self, saldo=1000):
        self.saldo = saldo
    
    def apostar_numero(self, cantidad, numero, resultado, ruleta):
        self.saldo -= cantidad
        if resultado == numero and resultado != 0:
            self.saldo += cantidad * 36
        ruleta.numero(cantidad, numero)

    def apostar_par(self, cantidad, paridad, resultado, ruleta):
        self.saldo -= cantidad
        if resultado%2 == paridad and resultado != 0:
            self.saldo += cantidad * 2
        ruleta.par(cantidad, paridad)