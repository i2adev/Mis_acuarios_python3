"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      11/06/2025
Commentarios:
    Módulo que contiene una clase derivada de QMenu. Esta clase contiene un
    menú contextual que permite cargar o eliminar un registro de la tabla.
"""

# Importaciones
from PyQt6.QtWidgets import QMenu, QTableView

class TableMenuContextual(QMenu):
    """ Menú contextual de la tabla. """

    def __init__(self, table: QTableView):
        """ COnstructor de clase. """

        # Llamamos al constructor base
        super().__init__()

        # Inicializamos las propiedades
        self.table = table

        # # Creamos el menú
        # action_cargar = QAction("CARGAR REGISTRO", self)
        # action_eliminar = QAction("ELIMINAR REGISTRO", self)
        #
        # # Armamos el menú
        # self.addAction(action_cargar)
        # self.addAction(action_eliminar)

