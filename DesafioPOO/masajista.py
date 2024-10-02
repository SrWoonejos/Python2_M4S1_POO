#clase que deriva a Masajista
class Masajista(Persona):
    def __init__(self, nombre, edad, nacionalidad, especialidad):
    super().__init__(noombre, edad, nacionalidad)
    self.especialidad = especialidad

def dar_masaje(self):
    print(f'{self.nombre} está dando un masaje.')
