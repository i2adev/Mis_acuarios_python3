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
from PyQt6.QtWidgets import (QLineEdit, QTextEdit, QPlainTextEdit, QWidget,
                             QTableView, QComboBox, QHeaderView, QMessageBox)
import enchant  # Enchant es la librería de revisión orográfica

from Model.DAO.base_dao import BaseDAO
from Model.Entities.base_entity import BaseEntity

class BaseController(QObject):
    """ Controlador base de la que hereda el resto de controladores. """

    def __init__(self, view: QWidget, dao: BaseDAO, mod: BaseEntity):
        """
        Constructor base

        Parámetros:
        :param view: Vista que hereda de BaseView
        :param dao: DAO de la entidad que hereda de BaseDAO
        :param mod: Modelo de la entidad que hereda de BaseEntity
        """

        super().__init__()

        self._view = view
        self._dao = dao
        self._mod = mod

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

    def _select_row_by_id(self, table: QTableView, id_elem: int,
                          column: int = 0):
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

    def _clean_view(self, control: QWidget):
        """ Limpia los controles del formulario. """

        # Limpia los controles del formulario
        for widget in self._view.findChildren(QWidget):
            # En caso de que sean controles de edición de textgo
            if isinstance(widget, self._text_widgets):
                widget.clear()

            # En caso de que sean combos
            if isinstance(widget, QComboBox):
                widget.setCurrentIndex(-1)

        # Establecemos el foco en el control
        control.setFocus()

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

    def _configure_table(self, table: QTableView):
        """ Configura l atabla de datos. """

        # Selecciona un afila entera
        table.setSelectionBehavior(
            QTableView.SelectionBehavior.SelectRows)

        # Solo se puede seleccionar uan fila
        table.setSelectionMode(
            QTableView.SelectionMode.SingleSelection)

        # Color de las filas alternadas
        table.setAlternatingRowColors(True)

        # Oculta las líneas de la tabla
        table.setShowGrid(False)

        # Elimina el tabulador
        table.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        # Ocultar la columna ID (columna 0)
        table.setColumnHidden(0, True)

        # Hacer que la columna de descripcion use el espaciorestante
        last_column_ix = table.model().columnCount() - 1
        header = table.horizontalHeader()
        header.setSectionResizeMode(last_column_ix, QHeaderView.ResizeMode.Stretch)

        # Mostrar puntos suspensivos si el texto no cabe
        table.setTextElideMode(Qt.TextElideMode.ElideRight)

    def _configure_table_foot(self):
        """ Configura el pie de la tabla. """

        self._view.label_total_pages.setText(str(self._pag.total_pages))
        self._fill_combo_page()

    def _next_page(self, event: QEvent) -> None:
        """ Pasa a la siguiente página de la tabla. """

        page_to = self._view.combo_select_page.currentData() + 1

        if page_to > self._pag.total_pages:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "SE HA LLEGADO A LA ÚLTIMA PÁGINA"
            )
            return

        self._pag.current_page = page_to
        self._view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def _previous_page(self, event: QEvent) -> None:
        """ Pasa a la anterior página de la tabla. """

        page_to = self._view.combo_select_page.currentData() - 1

        if page_to < 1:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "SE HA LLEGADO A LA PRIMERA PÁGINA"
            )
            return

        self._pag.current_page = page_to
        self._view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def _first_page(self, event: QEvent) -> None:
        """ Pasa a la primera página de la tabla. """

        page_to = 1

        if self._pag.current_page == 1:
            return

        self._pag.current_page = page_to
        self._view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def _last_page(self, event: QEvent) -> None:
        """ Pasa a la primera página de la tabla. """

        page_to = self._pag.total_pages

        if self._pag.current_page == self._pag.total_pages:
            return

        self._pag.current_page = page_to
        self._view.combo_select_page.setCurrentIndex(self._pag.page_index)

    def _fill_combo_page(self):
        """ Rellena el combo de selección de página. """

        self._view.combo_select_page.clear()
        for i in range(1, self._pag.total_pages + 1):
            self._view.combo_select_page.addItem(str(i), i)

