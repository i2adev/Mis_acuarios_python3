"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      14/09/2026
Comentarios:
    Módulo que contiene la vista de la entidad TIPO DE CONTROL DE TEMPERATURA.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Main.Views.base_view import BaseView
from ModuloMaestro.Views.Forms.tipo_control_temperatura_form import \
    TipoControlTemperaturaForm
from ModuloMaestro.Views.Forms.tipo_iluminacion_form import TipoIluminacionForm


class TipoControlTemperaturaView(BaseView):
    """ Formulario de tipo de control de temperatura. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = TipoControlTemperaturaForm()
        self.layout_form_data.addWidget(self.frame)
        self.set_tab_order()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las políticas de focus
        self.frame.edit_tipo_control_temperatura.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(self.frame.edit_tipo_control_temperatura,
                         self.frame.text_descripcion)


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = TipoControlTemperaturaView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
