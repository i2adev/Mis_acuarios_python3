"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      15/04/2026
Comentarios:
    Subclase personalizada de QPlainTextEdit diseñada para gestionar
    valores nulos y validación de longitud.
"""

from PyQt6.QtWidgets import QPlainTextEdit, QMessageBox


class PlainTextEdit(QPlainTextEdit):
    """ QPlainTextEdit que acepta valores nulos. """

    def __init__(self, control_name: str, parent=None):
        super().__init__(parent)

        self.control_name = control_name
        self.max_length = 4096
        self._value: str | None = None

    # =========================
    # API pública
    # =========================
    def value(self) -> str | None:
        """ Devuelve el valor como str o None si está vacío. """

        if self._value is None:
            return None

        return self._value

    def setValue(self, value: str | None):
        """ Establece un valor y actualiza la visualización. """

        if value is None or not value.strip():
            self._value = None
            self.blockSignals(True)
            self.clear()
            self.blockSignals(False)
            return

        value = value.strip()

        if len(value) > self.max_length:
            value = value[:self.max_length - 3] + "..."

        self._value = value

        self.blockSignals(True)
        self.setPlainText(self._value)
        self.blockSignals(False)

    # =========================
    # Eventos
    # =========================
    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self._on_edit_finished()

    # =========================
    # Lógica interna
    # =========================
    def _on_edit_finished(self):
        """ Equivalente a editingFinished para QPlainTextEdit """

        text = self.toPlainText().strip()

        # Caso vacío
        if not text:
            self._value = None
            self.blockSignals(True)
            self.clear()
            self.blockSignals(False)
            return

        # Validación longitud
        if len(text) > self.max_length:
            QMessageBox.warning(
                self,
                "ERROR DE VALIDACIÓN",
                f"EL CAMPO '{self.control_name}' ADMITE UN "
                f"MÁXIMO DE {self.max_length} CARACTERES.\n"
                "SE REDUCIRÁ EL CAMPO AL MÁXIMO PERMITIDO."
            )
            text = text[:self.max_length - 3] + "..."

        # Guardar valor interno
        self._value = text

        # Reflejar en UI sin disparar señales
        cursor = self.textCursor()
        pos = cursor.position()

        self.blockSignals(True)
        self.setPlainText(self._value)
        self.blockSignals(False)

        # Restaurar posición del cursor
        cursor.setPosition(min(pos, len(self._value)))
        self.setTextCursor(cursor)
