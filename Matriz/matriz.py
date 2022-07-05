import doctest
import numpy as np

DIMENSION = 5
MAX_NUM = 6
LARGO_SECUENCIA = 4
DESFASAJE_RECORRIDO = 2

class Nodo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Valor de x = %i.\nValor de y = %i" %(self.x, self.y)

class Secuencia:
    def __init__(self, nodo_inicio, nodo_fin):
        self.nodo_inicio = nodo_inicio
        self.nodo_fin = nodo_fin

    def __str__(self):
        return "Secuencia iniciada en (%i, %i) y finalizada en (%i, %i)" %(self.nodo_inicio.x, self.nodo_inicio.y, self.nodo_fin.x, self.nodo_fin.y)

#Crea y devuelve una matriz de tope_fil x tope_col con valores entre 0 y numero_maximo
def matriz_de_numeros_aleatorios(tope_fil, tope_col, numero_maximo):
    """
    >>> matriz = matriz_de_numeros_aleatorios(5, 5, 5)
    >>> es_valor_valido = True
    >>> for i in range(5):
    ...     for j in range(5):
    ...         es_valor_valido = es_valor_valido and matriz[i][j] >= 0 and matriz[i][j] <= 5
    >>> print(es_valor_valido)
    True
    """

    matriz_de_numeros = np.random.randint(0, numero_maximo, size = (tope_fil, tope_col))

    return matriz_de_numeros

#Devuelve True si ambos números son consecutivos (diferencia de 1 entre el absoluto de la resta)
#Devuelve False en cualquier otro caso
def son_numeros_consecutivos(numero, numero_a_verificar):
    """
    >>> son_numeros_consecutivos(0, 1)
    True

    >>> son_numeros_consecutivos(0, 0)
    False

    >>> son_numeros_consecutivos(1, 0)
    True

    >>> son_numeros_consecutivos(0, 2)
    False
    """
    return abs(numero - numero_a_verificar) == 1

#Busca una secuencia de largo 4 hacia abajo y hacia la derecha de un nodo de una matriz
def hallar_secuencia_consecutiva(numeros, nodo):
    """
    >>> hallar_secuencia_consecutiva([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], Nodo(0, 0))
    
    >>> hallar_secuencia_consecutiva([[5, 4, 5, 4, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], Nodo(0, 0))
    Secuencia iniciada en (0, 0) y finalizada en (0, 3)

    >>> hallar_secuencia_consecutiva([[5, 4, 5, 4, 3], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], Nodo(0, 0))
    Secuencia iniciada en (0, 0) y finalizada en (0, 3)

    >>> hallar_secuencia_consecutiva([[5, 0, 0, 0, 0], [4, 0, 0, 0, 0], [5, 0, 0, 0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]], Nodo(0, 0))
    Secuencia iniciada en (0, 0) y finalizada en (3, 0)

    >>> hallar_secuencia_consecutiva([[5, 0, 0, 0, 0], [4, 0, 0, 0, 0], [5, 0, 0, 0, 0], [4, 0, 0, 0, 0], [3, 0, 0, 0, 0]], Nodo(0, 0))
    Secuencia iniciada en (0, 0) y finalizada en (3, 0)

    >>> hallar_secuencia_consecutiva([[5, 1, 2, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], Nodo(0, 1))
    Secuencia iniciada en (0, 1) y finalizada en (0, 4)

    >>> hallar_secuencia_consecutiva([[5, 5, 0, 0, 0], [0, 1, 0, 0, 0], [0, 2, 0, 0, 0], [0, 3, 0, 0, 0], [0, 4, 0, 0, 0]], Nodo(1, 1))
    Secuencia iniciada en (1, 1) y finalizada en (4, 1)
    """

    es_consecutivo = True
    i = nodo.x
    j = nodo.y
    
    if nodo.x + LARGO_SECUENCIA <= DIMENSION:
        while i < DIMENSION - DESFASAJE_RECORRIDO + nodo.x and es_consecutivo:
            es_consecutivo = son_numeros_consecutivos(numeros[i][j], numeros[i+1][j])
            i += 1

        if es_consecutivo:
            print(Secuencia(nodo, Nodo(i, j)))

    es_consecutivo = True
    i = nodo.x
    j = nodo.y

    if nodo.y + LARGO_SECUENCIA <= DIMENSION:
        while j < DIMENSION - DESFASAJE_RECORRIDO + nodo.y and es_consecutivo:
            es_consecutivo = son_numeros_consecutivos(numeros[i][j], numeros[i][j+1])
            j += 1

        if es_consecutivo:
            print(Secuencia(nodo, Nodo(i, j)))

#Crea una matriz de DIMENSION x DIMENSION de números aleatorios (entre 0 y MAX_NUM).
#Muestra por pantalla el nodo inicio y fin de aquellas secuencias de números consecutivos y de largo 4.
def numeros_consecutivos():
    numeros = matriz_de_numeros_aleatorios(DIMENSION, DIMENSION, MAX_NUM)       #Elijo un máximo de MAX_NUM de forma arbitraria para aumentar las chances de 

    print(numeros)

    for i in range(DIMENSION):
        for j in range(DIMENSION):
            hallar_secuencia_consecutiva(numeros, Nodo(i, j))
           
if __name__ == "__main__":
    doctest.testmod(verbose = True, optionflags = doctest.IGNORE_EXCEPTION_DETAIL)