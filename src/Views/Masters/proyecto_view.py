"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      08/08/2025
Commentarios:
    Módulo que contiene el formulario maestro de acuario.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Forms.image_form import ImageForm
from Views.Masters.base_view import BaseView
from Views.Forms.proyecto_form import ProyectoForm


class ProyectoView(BaseView):
    """
    Formulario maestro del PROYECTO.
    """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configuramos el formulario
        self.frame = ProyectoForm()
        self.frame.setMinimumWidth(650)
        self.frame_image = ImageForm(self, "FOTOGRAFIAS_PROYECTO")
        self.frame_image.setFixedWidth(450)
        self.layout_form_data.addWidget(self.frame)
        self.layout_form_data.addWidget(self.frame_image)

        self.set_tab_order()

        # Asigna atajos de teclado
        self.button_insert.setShortcut("Ctrl+I")

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las politicas de focus
        self.frame.edit_nombre_proyecto.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_estado_proyecto.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.date_inicio.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.date_fin.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_motivo_cierre.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(
            self.frame.edit_nombre_proyecto, self.frame.combo_estado_proyecto
        )
        self.setTabOrder(
            self.frame.combo_estado_proyecto, self.frame.date_inicio
        )
        self.setTabOrder(
            self.frame.date_inicio, self.frame.date_fin
        )
        self.setTabOrder(
            self.frame.date_fin, self.frame.edit_motivo_cierre
        )
        self.setTabOrder(
            self.frame.edit_motivo_cierre, self.frame.text_descripcion
        )

# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ProyectoView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())