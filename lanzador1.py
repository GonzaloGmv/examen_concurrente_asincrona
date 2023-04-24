import time
from simulacion_bancaria import Cuenta

def main1():
    cuenta = Cuenta()
    print("Actualmente tiene en la cuenta", cuenta.saldo, "€")
    print("Realizando ingresos y retiradas...")
    time.sleep(1)
    for i in range(40):
        cuenta.ingresar(100)
    for i in range(20):
        cuenta.ingresar(50)
    for i in range(60):
        cuenta.ingresar(20)
    for i in range(40):
        cuenta.retirar(100)
    for i in range(20):
        cuenta.retirar(50)
    for i in range(60):
        cuenta.retirar(20)
    print("Ingresos y retiradas realizados")
    print("Actualmente tiene en la cuenta", cuenta.saldo, "€")


main1()
