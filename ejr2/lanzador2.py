import random
from simulador_casino import Ruleta, Jugador

ruleta = Ruleta()
jugador1 = Jugador()
n1 = random.randrange(0,37)
jugador1.apostar(10, n1, ruleta.lanzar(10, n1))
print("Saldo del jugador 1: ", jugador1.saldo)
print("Saldo de la ruleta: ", ruleta.saldo)