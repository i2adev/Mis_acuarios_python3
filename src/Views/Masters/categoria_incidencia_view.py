"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      24/07/2025
Commentarios:
    Módulo que contiene el formulario maestro de la categoría de incidencia.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Masters.base_view import BaseView
from Views.Forms.categoria_incidencia_form import CategoriaIncidenciaForm


class CategoriaIncidenciaView(BaseView):
    """
    Formulario maestro de la CATEGORÍA DE INCIDENCIA.
    """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configuramos el formulario
        self.frame = CategoriaIncidenciaForm()
        self.layout_form_data.addWidget(self.frame)
        self.set_tab_order()

        # Asigna atajos de teclado
        self.button_insert.setShortcut("Alt+I")

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las politicas de focus
        self.frame.edit_categoria_incidencia.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus
        )
        self.frame.text_observaciones.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus
        )

        # Establecer el orden
        self.setTabOrder(
            self.frame.edit_categoria_incidencia, self.frame.text_observaciones
        )

# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = CategoriaIncidenciaView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())