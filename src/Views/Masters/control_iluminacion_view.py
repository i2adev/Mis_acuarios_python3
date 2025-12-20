"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      20/12/2025
Comentarios:
    Módulo que contiene la vista de la entidad CONTROL DE ILUMINACIÓN.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Forms.control_iluminacion_form import ControlIluminacionForm
from Views.Masters.base_view import BaseView


class ControlIluminacionView(BaseView):
    """ Formulario de control de iluminación. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = ControlIluminacionForm()
        self.layout_form_data.addWidget(self.frame)
        self.set_tab_order()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las políticas de focus
        self.frame.edit_control_iluminacion.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(self.frame.edit_control_iluminacion,
                         self.frame.text_descripcion)


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ControlIluminacionView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
