#sub clase

class Futbolista(Persona):
    def __init__(self, nombre, edad, nacionalidad, posicion, goles):
        super().__init__(nombre, edad, nacionalidad)
        self.posicion = posicion
        self.goles = goles

#metodo jugador
    def entrenar(self):
        print(f'{self.nombre} está entrenando.')

    def jugar_partido(self):
        print(f'{self.nombre} está jugando un partido.')