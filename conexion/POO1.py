class Miclase:
    #atributos
    atributo1 = "Valor1"
    atributo2 = 0
    
    #metodos
    def metodo1(self):
        print("¡Hola desde el metodo1!")
        
    def metodo2(self, parametro):
        self.atributo2 = parametro
        print(f"El atrivuto es2 se actualizo a:  {self.atributo2}")
        
#creacion de un objeto a partir de la clase
obejeeto1= Miclase()
obejeeto2= Miclase()

#acceso a atributos  llamdas a metodos
print(obejeeto1.atributo1)   #salida: valor1
obejeeto1.metodo1()   #salida: ¡Hola desde el metodo1!

obejeeto2.metodo2(42)  #salida: El atrivuto es2 se actualizo a:  42
print(obejeeto2.atributo2)   #salida: 42
# Crear más objetos
objeto3 = Miclase()
objeto4 = Miclase()

# Definir métodos adicionales en la clase
def metodo3(self):
    print(f"Este es el metodo3. atributo1: {self.atributo1}, atributo2: {self.atributo2}")

def metodo4(self, nuevo_valor):
    self.atributo1 = nuevo_valor
    print(f"atributo1 actualizado a: {self.atributo1}")

# Agregar los nuevos métodos a la clase
setattr(Miclase, "metodo3", metodo3)
setattr(Miclase, "metodo4", metodo4)

# Usar los nuevos métodos con los nuevos objetos
objeto3.metodo3()
objeto4.metodo4("NuevoValor")
objeto4.metodo3()