"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      08/08/2025
Comentarios:
    Módulo que contiene el formulario maestro de urna.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Forms.image_form import ImageForm
from Views.Forms.urna_form import UrnaForm
from Views.Masters.base_view import BaseView


class UrnaView(BaseView):
    """
    Formulario maestro de la CATEGORÍA DE ACUARIO.
    """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configuramos el formulario
        self.frame = UrnaForm()
        self.frame.setMinimumWidth(650)
        self.frame_image = ImageForm(self, "FOTOGRAFIAS_URNA")
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

        # Establecemos las políticas de focus
        self.frame.combo_marca.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_modelo.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_ancho.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_profundo.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_alto.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_grosor.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_volumen.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_material.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(self.frame.combo_marca, self.frame.edit_modelo)
        self.setTabOrder(self.frame.edit_modelo, self.frame.edit_ancho)
        self.setTabOrder(self.frame.edit_ancho, self.frame.edit_profundo)
        self.setTabOrder(self.frame.edit_profundo, self.frame.edit_alto)
        self.setTabOrder(self.frame.edit_alto, self.frame.edit_grosor)
        self.setTabOrder(self.frame.edit_grosor, self.frame.edit_volumen)
        self.setTabOrder(self.frame.edit_volumen, self.frame.combo_material)
        self.setTabOrder(self.frame.combo_material, self.frame.text_descripcion)


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = UrnaView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
