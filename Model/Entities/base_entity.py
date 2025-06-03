'''
Entidad base
'''
class BaseEntity:
    """ La clase base de las entidades """
    def get_type(self):
        """ Devuelve el tipo de la clase """
        return type(self).__name__
