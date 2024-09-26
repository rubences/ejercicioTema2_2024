import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        # Aquí puedes implementar la lógica para determinar la galaxia basada en las coordenadas
        # Por ejemplo, podrías usar un sistema de clasificación simple basado en cuadrantes
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia A"
        elif self.x < 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia B"
        elif self.x >= 0 and self.y < 0 and self.z >= 0:
            return "Galaxia C"
        elif self.x >= 0 and self.y >= 0 and self.z < 0:
            return "Galaxia D"
        else:
            return "Galaxia Desconocida"

    def distancia(self, otra_estrella):
        return math.sqrt((self.x - otra_estrella.x)**2 + (self.y - otra_estrella.y)**2 + (self.z - otra_estrella.z)**2)

    def main_function():
            # Crear estrellas
            estrella_A = Estrella(2, 3, 1)
            estrella_B = Estrella(4, 4, 4)
            estrella_C = Estrella(-3, -1, 0)

            # Imprimir estrellas
            print(f"Estrella A: {estrella_A}")
            print(f"Estrella B: {estrella_B}")
            print(f"Estrella C: {estrella_C}")

            # Determinar galaxias
            print(f"Galaxia de la estrella A: {estrella_A.galaxia()}")
            print(f"Galaxia de la estrella B: {estrella_B.galaxia()}")
            print(f"Galaxia de la estrella C: {estrella_C.galaxia()}")

            # Calcular y mostrar distancias
            print(f"Distancia entre A y B: {estrella_A.distancia(estrella_B)}")
            print(f"Distancia entre B y C: {estrella_B.distancia(estrella_C)}")

            # (Opcional) Encontrar la estrella más lejos del origen
            distancia_A = estrella_A.distancia(Estrella(0, 0, 0))
            distancia_B = estrella_B.distancia(Estrella(0, 0, 0))
            distancia_C = estrella_C.distancia(Estrella(0, 0, 0))

            max_distancia = max(distancia_A, distancia_B, distancia_C)
            if max_distancia == distancia_A:
                print("La estrella más lejos del origen es A")
            elif max_distancia == distancia_B:
                print("La estrella más lejos del origen es B")
            else:
                print("La estrella más lejos del origen es C")





