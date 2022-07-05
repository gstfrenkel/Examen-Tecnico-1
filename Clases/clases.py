import doctest
import numpy as np

class Circulo:

    @classmethod
    def radio_menor_igual_a_uno_error(self):
        return "No se puede tener un círculo con radio menor o igual a 0."

    #Actualiza el radio de un Círculo. El radio debe ser mayor a 0.
    def definir_nuevo_radio(self, radio):
        """
        >>> print(Circulo(5).definir_nuevo_radio(3))
        Círculo de radio 3.

        >>> Circulo(5).definir_nuevo_radio(0)
        Traceback (most recent call last):
        Exception: No se puede tener un círculo con radio menor o igual a 0.

        >>> Circulo(5).definir_nuevo_radio(-2)
        Traceback (most recent call last):
        Exception: No se puede tener un círculo con radio menor o igual a 0.       
        """

        if radio <= 0:
            raise Exception(Circulo.radio_menor_igual_a_uno_error())

        self.radio = radio
        return self

    #Instancia un nuevo Círculo de cierto radio. El radio debe ser mayor a 0.
    def __init__(self, radio):
        """
        >>> print(Circulo(5))
        Círculo de radio 5.

        >>> Circulo(0)
        Traceback (most recent call last):
        Exception: No se puede tener un círculo con radio menor o igual a 0.

        >>> Circulo(-2)
        Traceback (most recent call last):
        Exception: No se puede tener un círculo con radio menor o igual a 0.   
        """

        self.definir_nuevo_radio(radio)

    def __str__(self):
        return "Círculo de radio %i." %self.radio

    def area(self):
        """
        >>> Circulo(5).area()
        78.53981633974483

        >>> Circulo(3).area()
        28.274333882308138
        """

        return np.pi * self.radio ** 2

    def perimetro(self):
        """
        >>> Circulo(5).perimetro()
        31.41592653589793

        >>> Circulo(3).perimetro()
        18.84955592153876
        """

        return 2 * np.pi * self.radio

    #Instancia un nuevo Círculo con un radio multiplicador veces mayor. Multiplicador debe ser mayor a 0.
    def nuevo_circulo(self, multiplicador):
        """
        >>> print(Circulo(5).nuevo_circulo(3))
        Círculo de radio 15.

        >>> print(Circulo(5).nuevo_circulo(0))
        Traceback (most recent call last):
        Exception: No se puede tener un círculo con radio menor o igual a 0.

        >>> print(Circulo(5).nuevo_circulo(-2))
        Traceback (most recent call last):
        Exception: No se puede tener un círculo con radio menor o igual a 0.    
        """

        return Circulo(self.radio * multiplicador)


if __name__ == "__main__":
    doctest.testmod(verbose = True, optionflags = doctest.IGNORE_EXCEPTION_DETAIL)