class Magia:
    def __init__(self, lista):
        self.lista = lista

    def __str__(self):
        return str(self.lista)
    
    def magia_numerica(self):
        # Eliminar los elementos duplicados
        lista_unica = list(set(self.lista))
        
        # Ordenar la lista de mayor a menor
        lista_ordenada = sorted(lista_unica, reverse=True)
        
        # Eliminar todos los números impares
        lista_pares = [num for num in lista_ordenada if num % 2 == 0]
        
        # Sumar todos los números que quedan
        suma = sum(lista_pares)
        
        # Colocar esta suma como el primer elemento de la lista
        lista_final = [suma] + lista_pares
        
        # Verificar que la suma de todos los números a partir del segundo elemento es igual al primer número de la lista
        assert suma == sum(lista_final[1:]), "La suma de los elementos no coincide con el primer elemento"
        
        return lista_final

    def main_function3():
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10]
        magia = Magia(lista)
        resultado = magia.magia_numerica()
        print(resultado)

