"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/03/2026
Comentarios:
    Módulo que contiene el formulario maestro del requerimiento de CO2
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from ModuloMaestro.Views.Forms.requerimiento_co2_form import RequerimientoCO2Form
from Main.Views.base_view import BaseView


class RequerimientoCO2View(BaseView):
    """
    Formulario maestro del REQUERIMIENTO DE CO2.
    """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configuramos el formulario
        self.frame = RequerimientoCO2Form()
        self.layout_form_data.addWidget(self.frame)
        self.set_tab_order()

        # Asigna atajos de teclado
        self.button_insert.setShortcut("Ctrl+I")

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las políticas de focus
        self.frame.edit_requerimiento.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(
            self.frame.edit_requerimiento, self.frame.text_descripcion
        )


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = RequerimientoCO2View("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
