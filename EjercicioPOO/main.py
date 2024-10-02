# Definición de la clase Animal
class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def caminar(self):
        print(f"{self.nombre} está caminando.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

# Creación del objeto Perro
perro = Animal(nombre="Brando", raza="San Bernardo", edad=3, peso=30)

# Creación del objeto Gato
gato = Animal(nombre="Roll", raza="Persa", edad=4, peso=3)

# Mostrar características del Perro y Gato
print(f"Perro: Nombre: {perro.nombre}, Raza: {perro.raza}, Edad: {perro.edad} años, Peso: {perro.peso} kg.")
print(f"Gato: Nombre: {gato.nombre}, Raza: {gato.raza}, Edad: {gato.edad} años, Peso: {gato.peso} kg.")

# Ejemplo de comportamiento
perro.comer()
perro.caminar()
perro.dormir()

gato.comer()
gato.caminar()
gato.dormir()
