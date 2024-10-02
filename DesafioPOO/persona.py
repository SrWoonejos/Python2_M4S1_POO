#clase padre

class Persona:
def __init__(self, nombre, edad, nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad
    
#metodos comunes con presentacion de la pers.
def __str__(self):
    return (f'{self.nombre}, {self.edad} años, Nacionalidad: {self.nacionalidad}')


