"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      18/07/2025
Commentarios:
    Módulo que contiene el formulario maestro de la subcategoría de
    acuario.
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Masters.base_view import BaseView
from Views.Forms.subcategoria_acuario_form import SubcategoriaAcuarioForm


class SubcategoriaAcuarioView(BaseView):
    """
    Formulario maestro de la SUBCATEGORÍA DE ACUARIO.
    """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configuramos el formulario
        self.frame = SubcategoriaAcuarioForm()
        # self.frame_main.setFixedWidth(650)
        self.layout_form_data.addWidget(self.frame)
        self.set_tab_order()

        # Asigna atajos de teclado
        self.button_insert.setShortcut("Ctrl+I")

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las politicas de focus
        self.frame.combo_categoria_acuario.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus
        )
        self.frame.edit_subcategoria_acuario.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus
        )
        self.frame.text_observaciones.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus
        )

        # Establecer el orden
        self.setTabOrder(
            self.frame.combo_categoria_acuario,
            self.frame.edit_subcategoria_acuario
        )
        self.setTabOrder(
            self.frame.edit_subcategoria_acuario,
            self.frame.text_observaciones
        )

# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = SubcategoriaAcuarioView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())