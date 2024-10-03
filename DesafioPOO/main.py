# Clase Futbolista
class Futbolista:
    def __init__(self, id, nombre, apellido, edad, dorsal, demarcacion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dorsal = dorsal
        self.demarcacion = demarcacion

    def concentrarse(self):
        print(f'{self.nombre} {self.apellido} está concentrándose.')

    def viajar(self):
        print(f'{self.nombre} {self.apellido} está viajando.')

    def jugarPartido(self):
        print(f'{self.nombre} {self.apellido} está jugando un partido.')

    def entrenar(self):
        print(f'{self.nombre} {self.apellido} está entrenando.')

# Clase Entrenador
class Entrenador:
    def __init__(self, id, nombre, apellido, edad, idFederacion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.idFederacion = idFederacion

    def concentrarse(self):
        print(f'{self.nombre} {self.apellido} está concentrándose.')

    def viajar(self):
        print(f'{self.nombre} {self.apellido} está viajando.')

    def dirigirPartido(self):
        print(f'{self.nombre} {self.apellido} está dirigiendo un partido.')

    def dirigirEntrenamiento(self):
        print(f'{self.nombre} {self.apellido} está dirigiendo un entrenamiento.')

# Clase Masajista
class Masajista:
    def __init__(self, id, nombre, apellido, edad, titulacion, annosExperiencia):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.titulacion = titulacion
        self.annosExperiencia = annosExperiencia

    def concentrarse(self):
        print(f'{self.nombre} {self.apellido} está concentrándose.')

    def viajar(self):
        print(f'{self.nombre} {self.apellido} está viajando.')

    def darMasaje(self):
        print(f'{self.nombre} {self.apellido} está dando un masaje.')
