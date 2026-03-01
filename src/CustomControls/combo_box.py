"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      01/03/2026
Comentarios:
    Subclase personalizada de QComboBox que admite valores nulo
"""

from PyQt6.QtWidgets import QComboBox


class ComboBox(QComboBox):
    """ Clase derivada de QComboBox que admite valores nulos. """

    def __init__(self, control_name: str, parent=None):
        super(ComboBox, self).__init__(parent)

        self.control_name = control_name

    def setValue(self, value: str):
        pass

    def values(self) -> int | None:
        """ Devuelve el valor del item seleccionado en el combobox. """

        return int(self.currentData()) if self.currentIndex() != -1 else None
