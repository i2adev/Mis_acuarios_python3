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
                             QPlainTextEdit, QWidget, QTableView, QSizeGrip,
                             QComboBox)
import enchant  # Enchant es la librería de revisión orográfica

from Model.DAO.paginator import Paginator
from Model.Entities.base_entity import BaseEntity
from Views.base_view import BaseView

class BaseController(QObject):
    """ Controlador base de la que hereda el resto de controladores. """

    def __init__(self, view: QWidget):
        """ Constructor de clase """

        super().__init__()

        self._view = view
        self._spell_dict = enchant.Dict("en_EN")
        self._text_widgets = (QLineEdit, QTextEdit, QPlainTextEdit)


    """
    ********************************************************************
    ** GESTIÓN DE EVENTOS COMUNES A TODOS LOS CONTROLADORES           **
    ********************************************************************
    """

    def __text_normalize(self, obj: QWidget, event):
        """
        Normaliza el texto del widjej, eliminando los espacios iniciales
        y finales y convirtiendo el texto en mayúsculas:
        - Parametro OBJ: Widjet de texto a normalizar.
        - Parámetro EVENT: Evento generado por el widget.
        """

        if isinstance(obj, QLineEdit):
            if obj.text():
                # obj.setText(obj.text().strip().upper())
                obj.setText(obj.text().strip())

        if isinstance(obj, (QTextEdit, QPlainTextEdit)):
            if obj.toPlainText():
                # obj.setPlainText(obj.toPlainText().strip().upper())
                obj.setPlainText(obj.toPlainText().strip())

    # Maneja los diferentes tipos de eventos comunes de las diustintas
    # vistas
    def eventFilter(self, obj: QWidget, event):
        """ Maneja los eventos de la vista. """

        # Gestiona los eventos de perdida de foco de los controles de
        # texto para normalizar el texto
        if event.type() == QEvent.Type.FocusOut:
            if isinstance(obj, self._text_widgets):
                self.__text_normalize(obj, event)
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

    def _select_row_by_id(self, table: QTableView, id_elem: int, column: int = 0):
        """ Selecciona una fila por su ID. """

        # Obtenemos el modelo de la tabla
        model = table.model()

        # Recorremos la tabla
        for fila in range(model.rowCount()):
            # Obtenemos el índice
            index = model.index(fila, column)
            if str(index.data()) == str(id_elem):
                # Si el ID coincide con el parámetro
                table.selectRow(fila)
                table.scrollTo(index)

    def _clean_view(self):
        """ Limpia los controles del formulario. """

        # Limpia los controles del formulario
        for widget in self._view.findChildren(QWidget):
            # En caso de que sean controles de edición de textgo
            if isinstance(widget, self._text_widgets):
                widget.clear()

            # En caso de que sean combos
            if isinstance(widget, QComboBox):
                widget.setCurrentIndex(-1)

    def _fill_combo(self, combo: QComboBox, lista: list[BaseEntity], attr_text: str, attr_data: str):
        """
        Llena un QComboBox con una lista de entidades.

        Parámetros:
        :param combo: El QComboBox que quieres llenar.
        :param lista: Lista de entidades (pueden ser objetos o diccionarios).
        :param attr_text: Nombre del atributo para el texto visible.
        :param attr_data: Nombre del atributo para el valor (userData).
        """

        combo.clear()
        for item in lista:
            # Si es diccionario
            if isinstance(item, dict):
                texto = item.get(attr_text, "")
                data = item.get(attr_data, None)
            else:
                texto = getattr(item, attr_text, "")
                data = getattr(item, attr_data, None)

            combo.addItem(texto, data)