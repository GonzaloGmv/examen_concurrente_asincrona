class Cuenta:
    def __init__(self, saldo = 100):
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo += cantidad
    
    def retirar(self, cantidad):
        self.saldo -= cantidad