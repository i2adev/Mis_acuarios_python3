"""
Conjtrolador base de la que heredan el resto de controladorese
"""

# Importaciones
from PyQt6.QtCore import QObject, QEvent
from PyQt6.QtWidgets import (QMessageBox, QLineEdit, QTextEdit,
                             QPlainTextEdit, QWidget)

class Base_controler(QObject):
    """ Controlador base """
    def __init__(self):
        """ Constructor de clase """
        super().__init__()
        self.text_widgets = (QLineEdit, QTextEdit, QPlainTextEdit)

    """
    ****************************************************************************
    ** GESTIÓN DE EVENTOS COMUNES A TODOS LOS CONTROLADORES                   **
    ****************************************************************************
    """

    def text_normalize(self, obj: QWidget, event):
        """
        Normaliza el texto del widjej, eliminando los espacios iniciales
        y finales y pconvirtiendo el texto en mayúsculas:
        -   Parametro OBJ: Widjet de texto a normalizar.
        -   Parámetro EVENT: Evento generado por el widget.
        """

        if isinstance(obj, QLineEdit):
            if obj.text() != "":
                obj.setText(obj.text().strip().upper())

        if isinstance(obj, (QTextEdit, QPlainTextEdit)):
            if obj.toPlainText() != "":
                obj.setPlainText(obj.toPlainText().strip().upper())

    # Maneja los diferentes tipos de eventos comunes de las diustintas vistas
    def eventFilter(self, obj: QWidget, event):
        """ Maneja los eventos de la vista """

        # Gestiona los eventos de perdida de foco de los controles de texto para
        # normalizar el texto
        if event.type() == QEvent.Type.FocusOut:
            if isinstance(obj, self.text_widgets):
                self.text_normalize(obj, event)
                return False # Dejamos que el widget maneje también su evento

        return super().eventFilter(obj, event)

