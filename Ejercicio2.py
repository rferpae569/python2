def main():
    print("PARES E IMPARES")
    numero1=int(input("Escriba un numero entero: "))
    numero2=int(input(f"Escriba un numero entero mayor o igual que {numero1}: "))

    if numero2 < numero1:

        print(f"¡Le he pedido un numero entero mayor o igual que {numero1}!")
    else:
        for i in range(numero1,numero2+1):
            if i%2 ==0:
                print(f"El numero {i} es par.")
            else:
                print(f"El numero {i} es impar.")

if __name__== "__main__":
    main()