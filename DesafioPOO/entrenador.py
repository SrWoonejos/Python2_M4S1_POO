#sub clase
class Entrenador(Persona):
    def __init__(self, nombre, edad nacionalidad, experiencia y estrategia):
        super().__init__(nombre, edad, nacionalidad)
        self.experiencia = experiencia
        self.estrategia = estrategia

    def dirigir_entrenamiento(self):
        print(f'{self.nombre} está dirigiendo un entrenamiento.')

    def dirigir_partido(self):
        print(f'{self.nombre} está dirigiendo un partido.')

        