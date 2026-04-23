"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      27/02/2026
Comentarios:
    Subclase personalizada de QLineEdit diseñada para manejar entrada de
    texto controlada, con validación de longitud, soporte de nulabilidad y
    transformación opcional a mayúsculas.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QMessageBox

from Services.Validators.validator import Validator
from globales import LOCALE


class StrLineEdit(QLineEdit):
    """
    QLineEdit para textos
    """

    # MAX_DIGITS = 8

    def __init__(self, control_name: str, max_length: int,
                 is_nullable: bool = True, is_capital: bool = False,
                 parent=None):

        # Llama al constructor padre
        super().__init__(parent)

        # Configura el control
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.control_name = control_name
        self.max_length = max_length
        self.is_nullable = is_nullable
        self.is_capital = is_capital
        self._value = None

        # Configura los eventos
        self.editingFinished.connect(self._on_edit_finished)

    def value(self):
        """ Devuelve el valor como str o None si está vacío. """

        if self._value:
            if self.is_capital:
                return self._value.upper()
            else:
                return self._value
        else:
            return None

    def setValue(self, value: str | None):
        """ Establece un valor y actualiza la visualización. """

        if value is None:
            self._value = None
            self.setText("")
        else:
            self._value = value if not self.is_capital else value.upper()
            self.setText(self._value)

    def _on_edit_finished(self):
        text = self.text().strip()

        if not text:
            self._value = None
            return

        # Valida el campo
        if len(text) > self.max_length:
            QMessageBox.warning(self, "ERROR DE VALIDACIÓN",
                                f"EL CAMPO '{self.control_name}' ADMITE UN "
                                f"MÁXIMO DE {self.max_length} CARACTERES.\n"
                                "SE REDUCIRÁ EL CAMPO AL MÁXIMO PERMITIDO.")
            self._value = text[:self.max_length - 3] + ("...")

        # Establecemos el texto
        self._value = text if not self.is_capital else text.upper()
        self.setText(self._value)
