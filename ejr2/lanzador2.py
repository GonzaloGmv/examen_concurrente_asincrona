import random
from ejr2.simulador_casino import Ruleta, Jugador

def main2():
    ruleta = Ruleta()
    jugador1 = Jugador()
    jugador2 = Jugador()
    ruleta.lanzar()
    jugador1.apostar_numero(10, random.randrange(1,37), ruleta.resultado, ruleta)
    jugador2.apostar_par(10, random.randrange(1,37), ruleta.resultado, ruleta)
    print("Saldo del jugador 1: ", jugador1.saldo)
    print("Saldo del jugador 2: ", jugador2.saldo)
    print("Saldo de la ruleta: ", ruleta.saldo)
    jugador3 = Jugador()
    apuesta = 10
    while jugador3.saldo<=1000 and jugador3.saldo>apuesta and ruleta.saldo>apuesta*36:
        jugador3.apostar_numero(apuesta, random.randrange(1,37), ruleta.resultado, ruleta)
        apuesta *= 2
        ruleta.lanzar()
    print("Saldo del jugador 3: ", jugador3.saldo)
    print("Saldo de la ruleta: ", ruleta.saldo)

#he estado haciendolo con threads pero no me da tiempo a terminarlo, lo dejo asimpara que no este a medias