"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contien la clase base de las entidades.
"""

class BaseEntity:
    """ La clase base de las entidades. """
    def get_type(self):
        """ Devuelve el tipo de la clase. """
        return type(self).__name__
