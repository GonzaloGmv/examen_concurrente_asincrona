import random

class Ruleta:
    def __init__(self, saldo=50000, resultado=None):
        self.saldo = saldo
        self.resultado = resultado
    
    def lanzar(self):
        self.resultado = random.randrange(0, 37)

    def numero(self, cantidad, numero):
        if self.resultado != numero:
            self.saldo += cantidad
        elif self.saldo < cantidad * 36:
            self.saldo -= cantidad * 36
        else:
            print("No hay suficiente saldo en la ruleta")
        return self.resultado
    
    def par(self, cantidad, paridad):
        if self.resultado%2 != paridad:
            self.saldo += cantidad
        elif self.saldo < cantidad * 2:
            self.saldo -= cantidad * 2
        else:
            print("No hay suficiente saldo en la ruleta")
        return self.resultado
    

class Jugador:
    def __init__(self, saldo=1000):
        self.saldo = saldo
    
    def apostar_numero(self, cantidad, numero, resultado, ruleta):
        self.saldo -= cantidad
        if ruleta.saldo <= cantidad * 36:
            print("No hay suficiente saldo en la ruleta")
        elif resultado == numero:
            self.saldo += cantidad * 36
        
        ruleta.numero(cantidad, numero)

    def apostar_par(self, cantidad, paridad, resultado, ruleta):
        self.saldo -= cantidad
        if ruleta.saldo <= cantidad * 2:
            print("No hay suficiente saldo en la ruleta")
        elif resultado%2 == paridad:
            self.saldo += cantidad * 2
        ruleta.par(cantidad, paridad)