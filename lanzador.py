from ejr1.lanzador1 import main1
from ejr2.lanzador2 import main2

def main():
    ejr = input("Elija el ejercicio (1 o 2): ")
    if ejr == "1":
        main1()
    elif ejr == "2":
        main2()