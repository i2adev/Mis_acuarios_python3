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

    def setValue(self, value: int):
        """
        Establece el valor del combo pasandole el valor.
        :param value: Valor a seleccionar en el combo
        """

        idx = self.findData(value)

        if idx >= 0:
            self.setCurrentIndex(idx)
        else:
            self.setCurrentIndex(-1)

    def value(self) -> int | None:
        """ Devuelve el valor del item seleccionado en el combobox. """

        return int(self.currentData()) if self.currentIndex() != -1 else None

    def indexByText(self, text: str) -> int | None:
        """ Obtiene el índice del item con el texto pasado como parámetro."""

        index = self.findText(text)
        return index if index != -1 else None
