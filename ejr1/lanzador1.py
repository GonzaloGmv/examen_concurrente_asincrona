import time
from ejr1.simulacion_bancaria import Cuenta, operacion

def main1():
    cuenta = Cuenta()
    print("Actualmente tiene en la cuenta", cuenta.saldo, "€")
    print("Realizando ingresos y retiradas...")
    time.sleep(1)
    valores = [100]*40 + [50]*20 + [20]*60 + [-100]*40 + [-50]*20 + [-20]*60
    list(map(operacion, [cuenta]*len(valores), valores))
    print("Ingresos y retiradas realizados")
    print("Actualmente tiene en la cuenta", cuenta.saldo, "€")