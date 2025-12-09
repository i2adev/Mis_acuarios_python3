"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      21/07/2025
Comentarios:
    Módulo que contiene la vista de la entidad TIPO DE ACUARIO.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Forms.tipo_filtro_form import TipoFiltroForm
from Views.Masters.base_view import BaseView


class TipoFiltroView(BaseView):
    """ Formulario de tipo de acuario. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = TipoFiltroForm()
        self.layout_form_data.addWidget(self.frame)
        self.set_tab_order()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las políticas de focus
        self.frame.edit_tipo_filtro.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.text_observaciones.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(
            self.frame.edit_tipo_filtro, self.frame.text_observaciones
        )


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = TipoFiltroView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
