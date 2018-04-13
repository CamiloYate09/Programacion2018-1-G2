# Podemos llamar de un archivo una sola funcion
from Semana8.operaciones_vectores import producto_punto as pp

# Una lista
vector = [1, 2, 8, 9]
# print(vector)

# Una Matriz es una lista de listas
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)

# para editar una posición lo hacemos por filas y columnas
matrix[1][1] = 10


#
# # para imprimir su forma matricial
# for fila in matrix:
#     print(fila)

def vector_columna(matriz, indice):
    """
    (list of list of num, int) -> list of num

    Obtiene el vector columna para la matriz dada

    >>> vector_columna([[1,2,3], [4,5,6], [7,8,9]], 0)
    [1, 4, 7]

    >>> vector_columna([[1,2,3], [4,5,6], [7,8,9]], 2)
    [3, 6, 9]

    :param matriz: la matriz para extraer
    :param indice: el indice del vector columna
    :return: el vector generado
    """
    resultado = []
    for i in range(0, len(matrix)):
        resultado.append(matrix[i][indice])
    return resultado


def producto_matrices(matriz_a, matriz_b):
    """
    (list of list of num, list of list of num) -> list of list of num

    Calcula el producto de dos matrices

    >>> producto_matrices([[1,2],[3,4]], [[1,2],[3,4]])
    [[7, 10], [15, 22]]

    :param matriz_a: La primer matriz
    :param matriz_b: La segunda Matriz
    :return: matriz_a * matriz_b
    """
    matriz_resultante = []
    # Este for recorre las filas de A
    for i in range(0, len(matriz_a)):
        # Este for recorre las columnas de B
        vector_fila = []
        for j in range(0, len(matriz_b[0])):
            print('Fila de a', matriz_a[i])
            print('Columna de b', vector_columna(matriz_b, j))
            vector_fila.append(pp(matriz_a[i], vector_columna(matriz_b, j)))
        matriz_resultante.append(vector_fila)
    return matriz_resultante


print(producto_matrices([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
