"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      22/02/2026
Comentarios:
    IntLineEdit es un QLineEdit personalizado diseñado para manejar
    únicamente números enteros, con validación y formato específico para
    aplicaciones donde se requiere entrada numérica controlada.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QMessageBox

from Services.Validators.validator import Validator
from globales import LOCALE


class IntLineEdit(QLineEdit):
    """
    QLineEdit que solo admite enteros.
    """

    MAX_DIGITS = 12

    def __init__(self, control_name: str, min_value: int, max_value: int,
                 units: str | None = None, is_nullable: bool = True,
                 parent=None):

        # Llama al constructor padre
        super().__init__(parent)

        # Configura el control
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.control_name = control_name
        self.min_value = min_value
        self.max_value = max_value
        self.units = units
        self.is_nullable = is_nullable
        self._value = None

        # Configura los eventos
        self.editingFinished.connect(self._on_edit_finished)

    def value(self):
        """ Devuelve el valor como int o None si está vacío. """

        return self._value

    def setValue(self, value: int | None):
        """ Establece un valor y actualiza la visualización. """

        if value is None:
            self._value = None
            self.setText("")
        else:
            self._value = value
            formatted = "{:,}".format(value).replace(",", ".")
            self.setText(formatted)

    def keyPressEvent(self, event):
        """
        Permite solo dígitos y teclas de control, limita el número de dígitos.
        """

        # Teclas de control permitidas
        if event.key() in (
                Qt.Key.Key_Backspace,
                Qt.Key.Key_Delete,
                Qt.Key.Key_Left,
                Qt.Key.Key_Right,
                Qt.Key.Key_Home,
                Qt.Key.Key_End):
            super().keyPressEvent(event)
            return

        # Solo permitir dígitos
        if event.text().isdigit():
            digits_only = ''.join(filter(str.isdigit, self.text()))
            if len(digits_only) >= self.MAX_DIGITS:
                # Ignorar si ya alcanzamos el máximo
                event.ignore()
            else:
                super().keyPressEvent(event)
        else:
            event.ignore()

    def focusInEvent(self, event):

        super().focusInEvent(event)

        # Establece el texto en el campo
        if self._value is not None:
            self.setText(str(self._value))

        # Quitar selección
        self.deselect()

        # Mover cursor al final
        self.setCursorPosition(len(self.text()))

    def _on_edit_finished(self):
        text = self.text().strip()

        if not text:
            self._value = None
            return

        # convertir usando locale
        val, ok = LOCALE.toInt(text)

        if not ok:
            QMessageBox.warning(self,
                                "ERROR DE FORMATO",
                                f"EL '{self.control_name}' SOLO ADMITE "
                                f"NÚMEROS ENTEROS.")
            self._value = None
            self.clear()
            return

        # Validar el campo
        res = Validator.validate_integer_field(self)
        if res.is_success:
            self._value = val

            # convierte 1000 -> 1.000
            formatted = "{:,}".format(val).replace(",", ".")
            self.setText(formatted)
        else:
            QMessageBox.warning(self,
                                "ERROR DE VALIDACIÓN",
                                res.error_msg)
            self._value = None
            self.setFocus()
