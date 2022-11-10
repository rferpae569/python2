from random import randrange

a=randrange(2,11)
b=randrange(2,11)

respuesta=int(input(f"¿Cuanto es {a} x {b}? "))

if respuesta==a*b:
    print("¡Respuesta correcta!")
else:
    print("¡Respuesta incorrecta!")