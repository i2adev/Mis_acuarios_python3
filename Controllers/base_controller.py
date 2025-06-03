"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contiene el controlador base del que heredarán los otros
    controladores. Estra clase contiene los comportamientos de los
    elementos comunes a todas las ventanas como la barra de título.
"""

# Importaciones
from PyQt6.QtCore import QObject, QEvent
from PyQt6.QtWidgets import (QMessageBox, QLineEdit, QTextEdit,
                             QPlainTextEdit, QWidget)

class BaseController(QObject):
    """ Controlador base de la que hereda el resto de controladores. """
    def __init__(self):
        """ Constructor de clase """
        super().__init__()
        self.text_widgets = (QLineEdit, QTextEdit, QPlainTextEdit)

    """
    ********************************************************************
    ** GESTIÓN DE EVENTOS COMUNES A TODOS LOS CONTROLADORES           **
    ********************************************************************
    """

    def text_normalize(self, obj: QWidget, event):
        """
        Normaliza el texto del widjej, eliminando los espacios iniciales
        y finales y pconvirtiendo el texto en mayúsculas:
        -   Parametro OBJ: Widjet de texto a normalizar.
        -   Parámetro EVENT: Evento generado por el widget.
        """

        if isinstance(obj, QLineEdit):
            if not obj.text():
                obj.setText(obj.text().strip().upper())

        if isinstance(obj, (QTextEdit, QPlainTextEdit)):
            if not obj.toPlainText():
                obj.setPlainText(obj.toPlainText().strip().upper())

    # Maneja los diferentes tipos de eventos comunes de las diustintas vistas
    def eventFilter(self, obj: QWidget, event):
        """ Maneja los eventos de la vista. """

        # Gestiona los eventos de perdida de foco de los controles de texto para
        # normalizar el texto
        if event.type() == QEvent.Type.FocusOut:
            if isinstance(obj, self.text_widgets):
                self.text_normalize(obj, event)
                return False # Dejamos que el widget maneje también su
                             # evento.

        return super().eventFilter(obj, event)

