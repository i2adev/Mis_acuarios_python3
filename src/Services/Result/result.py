"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contiene la clase Result. Esta clase se utiliza para
    aplicar el patron result.
"""


# Importaciones

class Result:
    """
    Clase que gestiona las devoluciones de las funciones, siguiendo el
    patron result.
    """

    def __init__(self, value = None, is_success: bool = None,
                 error_msg: str = None):
        """ Constructor de clase. """
        self.value = value
        self.is_success = is_success
        self.error_msg = error_msg

    @staticmethod
    def success(value):
        """
        Devuelve un resultado válido.
        Parámetro VALUE: Este es el valor a devolver.
        """
        return Result(value, True, None)

    @staticmethod
    def failure(error_msg: str):
        """
        Devuelve un resultado fallido.
        Parámetro ERROR_MSG: La cadena del error.
        """
        return Result(None, False, error_msg)