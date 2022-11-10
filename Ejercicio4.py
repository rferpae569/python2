from random import randrange

seguir=""

while seguir=="":
    tirada1=randrange(1,6)
    tirada2=randrange(1,6)
    tirada3=randrange(1,6)

    print(f"Tirada: {tirada1} {tirada2} {tirada3}")

    seguir=input("Pulse Intro para volver a jugar, otra tecla e Intro para terminar: ")

    print()

    print("Programa terminado")