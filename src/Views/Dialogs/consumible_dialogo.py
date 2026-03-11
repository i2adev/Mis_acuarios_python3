"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      10/03/2026
Comentarios:
    Módulo que contiene el diálogo de la entidad CONSUMIBLE.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget
from Views.Dialogs.base_dialog import BaseDialog
from Views.Forms.consumible_form import ConsumibleForm
from Views.Forms.image_form import ImageForm


class ConsumibleDialog(BaseDialog):
    """ Diálogo de consumible. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = ConsumibleForm()
        self.frame_image = ImageForm(self, "FOTOGRAFIAS_CONSUMIBLE")
        self.frame.setFixedWidth(850)
        self.layout_form_data.addWidget(self.frame)
        self.layout_form_data.addWidget(self.frame_image)
        self.set_tab_order()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las políticas de focus
        self.frame.combo_marca.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_producto.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.combo_categoria.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_formato.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_contenido.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_unidad.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(self.frame.combo_marca,
                         self.frame.edit_producto)
        self.setTabOrder(self.frame.edit_producto, self.frame.combo_categoria)
        self.setTabOrder(self.frame.combo_categoria, self.frame.combo_formato)
        self.setTabOrder(self.frame.combo_formato,
                         self.frame.edit_contenido)
        self.setTabOrder(self.frame.edit_contenido, self.frame.combo_unidad)
        self.setTabOrder(self.frame.combo_unidad,
                         self.frame.text_descripcion)


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ConsumibleDialog("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
