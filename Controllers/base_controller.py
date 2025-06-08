"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Módulo que contiene el controlador base del que heredarán los otros
    controladores. Estra clase contiene los comportamientos de los
    elementos comunes a todas las ventanas como la barra de título.
"""

# Importaciones
from PyQt6.QtCore import Qt, QObject, QEvent
from PyQt6.QtWidgets import (QMessageBox, QLineEdit, QTextEdit,
                             QPlainTextEdit, QWidget)

from Views.base_view import BaseView

class BaseController(QObject):
    """ Controlador base de la que hereda el resto de controladores. """
    # def __init__(self, view: QWidget):
    def __init__(self, view: QWidget):
        """ Constructor de clase """

        super().__init__()
        self._view = view
        self._text_widgets = (QLineEdit, QTextEdit, QPlainTextEdit)


    """
    ********************************************************************
    ** GESTIÓN DE EVENTOS COMUNES A TODOS LOS CONTROLADORES           **
    ********************************************************************
    """

    def text_normalize(self, obj: QWidget, event):
        """
        Normaliza el texto del widjej, eliminando los espacios iniciales
        y finales y convirtiendo el texto en mayúsculas:
        - Parametro OBJ: Widjet de texto a normalizar.
        - Parámetro EVENT: Evento generado por el widget.
        """

        if isinstance(obj, QLineEdit):
            if obj.text():
                obj.setText(obj.text().strip().upper())

        if isinstance(obj, (QTextEdit, QPlainTextEdit)):
            if obj.toPlainText():
                obj.setPlainText(obj.toPlainText().strip().upper())

    # Maneja los diferentes tipos de eventos comunes de las diustintas
    # vistas
    def eventFilter(self, obj: QWidget, event):
        """ Maneja los eventos de la vista. """

        # Gestiona los eventos de perdida de foco de los controles de
        # texto para normalizar el texto
        if event.type() == QEvent.Type.FocusOut:
            if isinstance(obj, self._text_widgets):
                self.text_normalize(obj, event)
                return False # Dejamos que el widget maneje también su
                             # evento.

        # Gestiona los eventos de pulsación de teclas en los controles
        # de textp.
        if event.type() == QEvent.Type.KeyPress:
            if isinstance(obj, (QTextEdit, QPlainTextEdit)):

                if event.key() == Qt.Key.Key_Tab and not event.modifiers():
                    self._view.focusNextChild()
                    return True
                elif event.key() == Qt.Key.Key_Backtab:
                    self._view.focusPreviousChild()
                    return True
                elif (event.key() == Qt.Key.Key_Tab and event.modifiers()
                      == Qt.KeyboardModifier.ControlModifier):
                    cursor = obj.textCursor()
                    cursor.insertText("\t")
                    return True
                else:
                    return False

        return super().eventFilter(obj, event)

