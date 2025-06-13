class Coche:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El coche {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h")
#creacion de un ubjeto de tipo de coche
mi_coche = Coche("Toyota", "Corolla", 50)

#llamda a metodo acelerar
mi_coche.acelerar(20)  # Aumenta la velocidad en 20 km/h