import random
from simulador_casino import Ruleta, Jugador

ruleta = Ruleta()
jugador1 = Jugador()
jugador2 = Jugador()
n1 = random.randrange(0,37)
n2 = random.randrange(0,37)
ruleta.lanzar()
jugador1.apostar_numero(10, n1, ruleta.resultado, ruleta)
jugador2.apostar_par(10, 0, ruleta.resultado, ruleta)
print("Saldo del jugador 1: ", jugador1.saldo)
print("Saldo del jugador 2: ", jugador2.saldo)
print("Saldo de la ruleta: ", ruleta.saldo)