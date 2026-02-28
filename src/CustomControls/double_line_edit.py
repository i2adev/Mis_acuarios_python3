"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      25/02/2026
Comentarios:
    DoubleLineEdit es un QLineEdit personalizado diseñado para manejar
    únicamente números decimales, con validación y formato específico para
    aplicaciones donde se requiere entrada numérica controlada.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QMessageBox

from Services.Validators.validator import Validator
from globals import LOCALE


class DoubleLineEdit(QLineEdit):
    """
    QLineEdit que solo admite números decimales.
    """

    MAX_DIGITS = 8

    def __init__(self, control_name: str, min_value: int, max_value: int,
                 units: str, is_nullable: bool = True, parent=None):

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
        """ Devuelve el valor como float o None si está vacío. """

        return self._value

    def setValue(self, value: int | None):
        """ Establece un valor y actualiza la visualización. """

        if value is None:
            self._value = None
            self.setText("")
        else:
            self._value = value
            self.setText(LOCALE.toString(self._value))

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

        # Detectamos si se ha pulsado la coma
        if event.key() == Qt.Key.Key_Comma:
            n = self.text()
            if "," in n:
                QMessageBox.warning(
                    None,
                    "ERROR DE FORMATO",
                    "YA HAS INSERTADO LA COMA DECIMAL AL NÚMERO"
                )
                event.ignore()
            else:
                super().keyPressEvent(event)

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
            n = str(self._value).strip()
            n = n.replace(".", ",")
            self.setText(str(n))

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
        val, ok = LOCALE.toDouble(text)

        if not ok:
            QMessageBox.warning(self,
                                "ERROR DE FORMATO",
                                f"EL '{self.control_name}' SOLO ADMITE "
                                f"NÚMEROS DECIMALES.")
            self.clear()
            self._value = None
            return

        # Validar el campo
        res = Validator.validate_float_field(self)
        if res.is_success:
            self._value = val

            # convierte 1000.0 -> 1.000,0
            formatted = ("{:,.1f}".format(val)
                         .replace(",", "X")
                         .replace(".", ",")
                         .replace("X", "."))
            self.setText(formatted)
        else:
            QMessageBox.warning(self,
                                "ERROR DE VALIDACIÓN",
                                res.error_msg)
            self.clear()
            self.setFocus()
            self._value = None
