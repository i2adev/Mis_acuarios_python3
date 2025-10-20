"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      10/10/2025
Comentarios:
    QDateEdit personalizado que permite dejar el campo vacío (valor nulo)
    y seleccionar fecha mediante un calendario emergente integrado.
"""
from PyQt6.QtCore import QDate, Qt, QPoint, pyqtSignal, QRegularExpression, \
    QSize
from PyQt6.QtGui import QRegularExpressionValidator, QIcon, QPixmap
from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QToolButton, QCalendarWidget,
    QHBoxLayout, QApplication, QFrame
)

import Resources.image_rc


class NullableDateEdit(QWidget):
    """QDateEdit personalizado con calendario integrado y soporte para valor nulo."""

    date_changed = pyqtSignal(QDate)

    def __init__(self, parent=None):
        super().__init__(parent)

        # ───────────────────────────────
        # Layout principal
        # ───────────────────────────────
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(1)

        # Campo de texto (entrada manual)
        self.edit_date = QLineEdit()
        regex = QRegularExpression(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$|^$")
        validator = QRegularExpressionValidator(regex)
        self.edit_date.setValidator(validator)
        self.edit_date.textChanged.connect(self._on_text_changed)
        self.edit_date.editingFinished.connect(self._on_editing_finished)

        # Conectar eventos de foco
        self.edit_date.focusInEvent = self._on_focus_in
        self.edit_date.focusOutEvent = self._on_focus_out

        # Botón calendario
        self.button_calendar = QToolButton()
        # self.button_calendar.setText("📅")

        icon_calendar = QIcon()
        icon_calendar.addPixmap(QPixmap(":/Images/calendario.png"), QIcon.Mode.Normal,
                        QIcon.State.On)
        self.button_calendar.setIcon(icon_calendar)
        self.button_calendar.setIconSize(QSize(16, 16))
        self.button_calendar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button_calendar.setToolTip("Seleccionar fecha")
        self.button_calendar.setStyleSheet(
            """
            QToolButton {
                background-color: transparent;
                border: none;
                color: #666;
                padding: 2px;
            }
            QToolButton:hover {
                background-color: #e0e0e0;
            }
            QToolButton:pressed {
                background-color: #d0d0d0;
            }
            """
        )
        self.button_calendar.clicked.connect(self._toggle_calendar)

        # Botón limpiar
        self.button_clear = QToolButton()
        self.button_clear.setText("✕")
        self.button_clear.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button_clear.setToolTip("Limpiar fecha")
        self.button_clear.setStyleSheet(
            """
            QToolButton {
                background-color: transparent;
                border: none;
                font-weight: bold;
                color: #666;
                padding: 2px;
            }
            QToolButton:hover {
                color: #ff4444;
            }
            """
        )
        self.button_clear.clicked.connect(self.clear_date)
        self.button_clear.hide()

        layout.addWidget(self.edit_date)
        layout.addWidget(self.button_calendar)
        layout.addWidget(self.button_clear)

        # ───────────────────────────────
        # Estado interno
        # ───────────────────────────────
        self._current_date = QDate()
        self._display_format = "dd/MM/yyyy"
        self._calendar_visible = False
        self._has_focus = False

        # ───────────────────────────────
        # Calendario emergente
        # ───────────────────────────────
        self.calendar_popup = QFrame(self, Qt.WindowType.Popup)
        cal_layout = QHBoxLayout(self.calendar_popup)
        cal_layout.setContentsMargins(0, 0, 0, 0)
        self.calendar = QCalendarWidget(self.calendar_popup)
        cal_layout.addWidget(self.calendar)

        self.calendar.clicked.connect(self._on_calendar_date_selected)
        self.calendar_popup.hide()

        self._update_appearance()

    # ───────────────────────────────
    # EVENTOS DE FOCO
    # ───────────────────────────────
    def _on_focus_in(self, event):
        """Cuando el campo recibe el foco."""
        self._has_focus = True
        if self.isNull():
            self.edit_date.setPlaceholderText("dd/mm/aaaa")
        QLineEdit.focusInEvent(self.edit_date, event)

    def _on_focus_out(self, event):
        """Cuando el campo pierde el foco."""
        self._has_focus = False
        self.edit_date.setPlaceholderText("")
        QLineEdit.focusOutEvent(self.edit_date, event)

    # ───────────────────────────────
    # LÓGICA DEL CONTROL
    # ───────────────────────────────
    def _toggle_calendar(self):
        """Mostrar u ocultar el calendario emergente."""
        if self._calendar_visible:
            self.calendar_popup.hide()
            self._calendar_visible = False
        else:
            init_date = self._current_date if self._current_date.isValid() else QDate.currentDate()
            self.calendar.setSelectedDate(init_date)

            pos = self.mapToGlobal(self.button_calendar.pos() + QPoint(0, self.button_calendar.height()))
            self.calendar_popup.move(pos)
            self.calendar_popup.adjustSize()
            self.calendar_popup.show()
            self._calendar_visible = True

    def _on_calendar_date_selected(self, date: QDate):
        """Cuando el usuario selecciona una fecha en el calendario."""
        self.setDate(date)
        self.calendar_popup.hide()
        self._calendar_visible = False

    def _on_text_changed(self, text: str):
        """Cuando cambia el texto del campo."""
        if text == "":
            self._current_date = QDate()
            self.button_clear.hide()
            self.date_changed.emit(QDate())
            if self._has_focus:
                self.edit_date.setPlaceholderText("dd/mm/aaaa")
        else:
            self.button_clear.show()
            self.edit_date.setPlaceholderText("")

    def _on_editing_finished(self):
        """Validar texto manual."""
        text = self.edit_date.text()
        if text:
            date = QDate.fromString(text, self._display_format)
            if date.isValid():
                self.setDate(date)
            else:
                self.clear_date()

    def clear_date(self):
        """Dejar el campo vacío."""
        self._current_date = QDate()
        self.edit_date.clear()
        self.button_clear.hide()
        if self._has_focus:
            self.edit_date.setPlaceholderText("dd/mm/aaaa")
        self.date_changed.emit(QDate())

    def setDate(self, date: QDate | None):
        """Establecer una fecha."""
        if date and date.isValid():
            self._current_date = date
            self.edit_date.setText(date.toString(self._display_format))
            self.button_clear.show()
            self.date_changed.emit(date)
            self.edit_date.setPlaceholderText("")
        else:
            self.clear_date()

    def date(self) -> QDate:
        """Devolver la fecha actual o QDate() si está vacía."""
        return self._current_date

    def isNull(self) -> bool:
        """Comprobar si la fecha está vacía."""
        return not self._current_date.isValid()

    def _update_appearance(self):
        """Actualizar el estado visual."""
        if self._current_date.isValid():
            self.edit_date.setText(self._current_date.toString(self._display_format))
            self.button_clear.show()
            self.edit_date.setPlaceholderText("")
        else:
            self.edit_date.clear()
            self.button_clear.hide()
            if self._has_focus:
                self.edit_date.setPlaceholderText("dd/mm/aaaa")

    def setDisplayFormat(self, fmt: str):
        """Cambiar el formato de visualización."""
        self._display_format = fmt

    def displayFormat(self) -> str:
        return self._display_format


# ───────────────────────────────
# DEMO DE PRUEBA
# ───────────────────────────────
if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QDialog

    class ExampleDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("NullableDateEdit Integrado")
            self.setGeometry(100, 100, 300, 200)
            layout = QVBoxLayout(self)

            self.date_edit = NullableDateEdit()
            self.date_edit.date_changed.connect(self.on_date_changed)

            self.status_label = QLabel("Fecha: NULA")
            btn_today = QPushButton("Fecha actual")
            btn_today.clicked.connect(lambda: self.date_edit.setDate(QDate.currentDate()))

            btn_clear = QPushButton("Limpiar")
            btn_clear.clicked.connect(self.date_edit.clear_date)

            layout.addWidget(QLabel("Selecciona una fecha:"))
            layout.addWidget(self.date_edit)
            layout.addWidget(self.status_label)
            layout.addWidget(btn_today)
            layout.addWidget(btn_clear)

        def on_date_changed(self, date):
            if date.isValid():
                self.status_label.setText(f"Fecha: {date.toString('dd/MM/yyyy')}")
            else:
                self.status_label.setText("Fecha: NULA")

    app = QApplication(sys.argv)
    dlg = ExampleDialog()
    dlg.show()
    sys.exit(app.exec())
