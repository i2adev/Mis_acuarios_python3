"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/07/2025
Comentarios:
    Módulo que contiene el formulario maestro de la marca comercial.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QSpacerItem, QSizePolicy

from Views.Forms.marca_comercial_form import MarcaComercialForm
from Views.Masters.base_view import BaseView


class MarcaComercialView(BaseView):
    """
    Formulario maestro de la MARCA COMERCIAL.
    """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Establecemos los tamaños
        self.setMinimumSize(1400, 870)
        self.data_table.setMinimumHeight(200)

        # Configuramos el formulario
        self.frame = MarcaComercialForm()

        self.layout_form_data.addWidget(self.frame)
        self.layout_form_data.addSpacerItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Minimum)
        )
        self.set_tab_order()

        # Asigna atajos de teclado
        self.button_insert.setShortcut("Ctrl+I")

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las politicas de focus
        self.frame.edit_marca.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_direccion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_cod_postal.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_poblacion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_provincia.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_pais.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.text_observaciones.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(
            self.frame.edit_marca, self.frame.edit_direccion
        )
        self.setTabOrder(
            self.frame.edit_direccion, self.frame.edit_cod_postal
        )
        self.setTabOrder(
            self.frame.edit_cod_postal, self.frame.edit_poblacion
        )
        self.setTabOrder(
            self.frame.edit_poblacion, self.frame.edit_provincia
        )
        self.setTabOrder(
            self.frame.edit_provincia, self.frame.combo_pais
        )
        self.setTabOrder(
            self.frame.combo_pais, self.frame.text_observaciones
        )


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MarcaComercialView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
