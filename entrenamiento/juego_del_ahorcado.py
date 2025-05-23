import random

def obtener_palabra():
    palabras = ['python', 'programacion', 'ahorcado', 'computadora', 'teclado']
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

def juego_ahorcado():
    palabra = obtener_palabra()
    letras_adivinadas = set()
    intentos = 6

    print("¡Bienvenido al juego del ahorcado!")
    while intentos > 0:
        print(f"\nPalabra: {mostrar_tablero(palabra, letras_adivinadas)}")
        print(f"Intentos restantes: {intentos}")
        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue

        if letra in palabra:
            letras_adivinadas.add(letra)
            if all(l in letras_adivinadas for l in palabra):
                print(f"\n¡Felicidades! Has adivinado la palabra: {palabra}")
                break
        else:
            letras_adivinadas.add(letra)
            intentos -= 1
            print("Letra incorrecta.")

    else:
        print(f"\n¡Has perdido! La palabra era: {palabra}")

if __name__ == "__main__":
    juego_ahorcado()