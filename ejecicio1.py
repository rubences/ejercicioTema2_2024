import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia Alfa"
        elif self.x < 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia Beta"
        elif self.x >= 0 and self.y < 0 and self.z >= 0:
            return "Galaxia Gamma"
        elif self.x >= 0 and self.y >= 0 and self.z < 0:
            return "Galaxia Delta"
        else:
            return "Galaxia Desconocida"

    def distancia(self, otra_estrella):
        return math.sqrt((self.x - otra_estrella.x)**2 + (self.y - otra_estrella.y)**2 + (self.z - otra_estrella.z)**2)

# Creación de las estrellas
estrella_A = Estrella(2, 3, 1)
estrella_B = Estrella(4, 4, 4)
estrella_C = Estrella(-3, -1, 0)

# Imprimir las estrellas
print(f"Estrella A: {estrella_A}")
print(f"Estrella B: {estrella_B}")
print(f"Estrella C: {estrella_C}")

# Determinar galaxias
print(f"Galaxia de la estrella A: {estrella_A.galaxia()}")
print(f"Galaxia de la estrella B: {estrella_B.galaxia()}")
print(f"Galaxia de la estrella C: {estrella_C.galaxia()}")

# Calcular y mostrar distancias
distancia_A_B = estrella_A.distancia(estrella_B)
distancia_B_C = estrella_B.distancia(estrella_C)
print(f"Distancia entre A y B: {distancia_A_B}")
print(f"Distancia entre B y C: {distancia_B_C}")

# (Opcional) Encontrar la estrella más lejos del origen
distancia_A_origen = estrella_A.distancia(Estrella(0, 0, 0))
distancia_B_origen = estrella_B.distancia(Estrella(0, 0, 0))
distancia_C_origen = estrella_C.distancia(Estrella(0, 0, 0))

distancias = {
    "A": distancia_A_origen,
    "B": distancia_B_origen,
    "C": distancia_C_origen
}


estrella_mas_lejos = max(distancias, key=distancias.get)
print(f"La estrella más lejos del origen es la estrella {estrella_mas_lejos} con una distancia de {distancias[estrella_mas_lejos]}")