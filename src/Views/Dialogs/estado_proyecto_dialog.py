"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      21/07/2025
Comentarios:
    Módulo que contiene el diálogo de la entidad TIPO DE FILTRO.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Dialogs.base_dialog import BaseDialog
from Views.Forms.estado_proyecto_form import EstadoProyectoForm


class EstadoProyectoDialog(BaseDialog):
    """ Diálogo de estado de proyecto . """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = EstadoProyectoForm()
        self.frame.setFixedWidth(350)
        self.layout_form_data.addWidget(self.frame)
        self.set_tab_order()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las políticas de focus
        self.frame.edit_estado_proyecto.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.text_observaciones.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(
            self.frame.edit_estado_proyecto, self.frame.text_observaciones
        )


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = EstadoProyectoDialog("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
