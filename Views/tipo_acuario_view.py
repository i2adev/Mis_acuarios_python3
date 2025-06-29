"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      27/06/2025
Commentarios:
    Módulo que contiene la vista de la entidad TIPO DE ACUARIO.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QFrame, QWidget

from Views.base_view import BaseView
from Views.tipo_acuario_form import TipoAcuarioForm


class TipoAcuarioView(BaseView):
    """ Formulario de tipo de acuario. """

    def  __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = TipoAcuarioForm()
        self.layout_form_data.addWidget(self.frame)
        self.set_tab_order()



    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # # Eliminar el focus de los widgets que no lo necesitan
        # for widget in self.findChildren(QWidget):
        #     widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        #
        # # Establecemos las politicas de focus
        # self.edit_tipo_filtro.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        #
        # # Establecer el orden
        # self.setTabOrder(self.edit_tipo_filtro, self.text_observaciones)

# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = TipoAcuarioView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())