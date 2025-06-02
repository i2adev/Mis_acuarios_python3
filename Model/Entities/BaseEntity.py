'''
Entidad base
'''
class BaseEntity:

    def get_type(self):
        raise NotImplementedError("Debes de implementar el método en las clases derivadas de 'BaseEntity'.")

    # '''Clase base de la que heredarán todas las entidades'''
    # def __init__(self, id_bd = None):
    #     '''
    #     Constructor:
    #         Parámetro id = id de la entidad
    #     '''
    #     self.id=id_bd

    # def save(self):
    #     '''Método abstracto para almacenar la entidad en la BD'''
    #     raise NotImplementedError
    
    # @classmethod
    # def get(cls, id):
    #     '''Método abstracto para obtener la entidad por ID'''
    #     raise NotImplementedError
