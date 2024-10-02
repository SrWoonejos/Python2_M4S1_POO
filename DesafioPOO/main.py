#clase principal

#importar clases desde los modulos
from futbolista import Futbolista
from entrenador import Entrenador
from masajista import Masajista

#instancias de clases
futbolista = Futbolista("Lionel Messi", 36, "Argentina", "Delantero", 800)
entrenador = Entrenador("Pep Guardiola", 52, "España", "Posesión de balón", 15)
masajista = Masajista("John Doe", 45, "Inglaterra", "Fisioterapia", 20)

#metodos de clases
print("---Futbolista---")
futbolista.entrenar()
futbolista.jugar_partido()

print("---Entrenador---")
entrenador.dirigir_entrenamiento()
entrenador.dirigir_partido()

print("---Masajista---")
masajista.dar_masaje()

