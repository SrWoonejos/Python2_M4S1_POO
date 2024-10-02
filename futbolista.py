#sub clase

class Futbolista(Persona):
    def __init__(self, nombre, edad, nacionalidad, posicion, goles):
        super().__init__(nombre, edad, nacionalidad)
        self.posicion = posicion
        self.goles = goles

