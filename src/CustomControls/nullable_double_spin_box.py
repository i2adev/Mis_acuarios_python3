"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  21/02/2026
Comentarios:
    QSpinBox personalizado que permite gestionar valores nulos.
"""
from PyQt6.QtWidgets import QDoubleSpinBox


class NullableDOubleSpinBox(QDoubleSpinBox):
    """ Clase que hereda de QSpinBox que permite manejar valores nulos. """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGroupSeparatorShown(True)
        self.setDecimals(1)
        self.setMinimum(-1)
        self.setValue(-1)
        self.setSpecialValueText(" ")

    def get_value(self):
        """ Método para obtener el valor o None. """

        val = self.value()
        return None if val == -1 else val
