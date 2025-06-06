def verificar_numero(numero):
    if numero == 0:
        return "El número es 0"
    elif numero % 2 == 0:
        return f"El número {numero} es par"
    else:
        if numero % 3 == 0:
            return f"El número {numero} es impar y divisible entre 3"
        else:
            return f"El número {numero} es impar pero no es divisible entre 3"

# Ejemplo de uso
while True:
    try:
        entrada = input("Ingrese un número (o 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        num = int(entrada)
        print(verificar_numero(num))
    except ValueError:
        print("Por favor, ingrese un número válido o escriba 'salir' para terminar.")

print("Programa terminado.")