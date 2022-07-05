import doctest
import random as rd

MAX_EDADES = 10
MAX_EDAD = 100
MIN_EDAD = 1

#Agrega a la lista de edades un diccionario de clave = id y valor = número random entre MIN_EDAD Y MAX_EDAD
def agregar_edad(edades, id):
    """
    >>> a = []
    >>> agregar_edad(a, 0)
    >>> print(list(a[0].values())[0] >= MIN_EDAD and list(a[0].values())[0] <= MAX_EDAD)
    True
    """
    edad = {id: rd.randint(MIN_EDAD, MAX_EDAD)}

    edades.append(edad)

#Devuelve True si el valor de edad (diccionario) es mayor al de edad_a_verificar (diccionario).
#Devuelve False en cualquier otro caso
def es_edad_mayor(edad, edad_a_verificar):
    """
    >>> es_edad_mayor({4: 17}, {7: 25})
    False

    >>> es_edad_mayor({4: 25}, {7: 17})
    True

    >>> es_edad_mayor({4: 25}, {7: 25})
    False
    """
    valor_edad = list(edad.values())[0]
    valor_edad_a_verificar = list(edad_a_verificar.values())[0]

    return valor_edad > valor_edad_a_verificar

#Ordena ascendentemente edades (lista de tope 10 de diccioanrios) según valor de cada diccionario.
def ordenar_edades_ascendentemente(edades):
    """
    >>> a = [{0: 18}, {1: 2}, {2: 65}, {3: 35}, {4: 16}, {5: 12}, {6: 44}, {7: 39}, {8: 98}, {9: 21}]
    >>> es_mayor = True
    >>> ordenar_edades_ascendentemente(a)
    >>> for i in range(MAX_EDADES-1):
    ...     es_mayor = es_mayor and es_edad_mayor(a[i+1], a[i])
    >>> print(es_mayor)
    True
    """
    for i in range(MAX_EDADES):
        for j in range(MAX_EDADES - 1):
            if es_edad_mayor(edades[j], edades[j+1]):
                auxiliar = edades[j+1]
                edades[j+1] = edades[j]
                edades[j] = auxiliar

#Muestra por pantalla la clave del primer y último elemento de edades (lista de tope 10 de diccioanrios).
def mostrar_persona_mas_joven_y_anciana(edades):
    """
    >>> a = [{0: 18}, {1: 2}, {2: 65}, {3: 35}, {4: 16}, {5: 12}, {6: 44}, {7: 39}, {8: 98}, {9: 21}]
    >>> ordenar_edades_ascendentemente(a)
    >>> mostrar_persona_mas_joven_y_anciana(a)
    La persona más joven es la de id: 1
    La persona más anciana es la de id: 8
    """
    id_joven = list(edades[0].keys())[0]
    id_anciana = list(edades[MAX_EDADES-1].keys())[0]

    print("La persona más joven es la de id: %i" %id_joven)
    print("La persona más anciana es la de id: %i" %id_anciana)


#Devuelve una lista de tope 10 de diccionarios de personas (ordenadas ascendentemente según edad),donde las claves son sus ids y los valores las edades
#(número generado aleatoriamente).
#Muestra por pantalla los ids de la persona más joven y de la persona más anciana.
def edades():
    #Al depender edades() de la generación de números aleatorios, decido probar cada una de las funciones por separado.
    edades = []

    for i in range(MAX_EDADES):
        agregar_edad(edades, i)

    ordenar_edades_ascendentemente(edades)

    mostrar_persona_mas_joven_y_anciana(edades)

    return edades

if __name__ == "__main__":
    doctest.testmod(verbose = True, optionflags = doctest.IGNORE_EXCEPTION_DETAIL)