"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/03/2026
Comentarios:
    Módulo que contiene el formulario maestro de la posición de la planta 
    en el acuario.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Forms.posicion_planta_Acuario_form import PosicionPlantaAcuarioForm
from Views.Masters.base_view import BaseView


class PosicionPlantaAcuarioView(BaseView):
    """
    Formulario maestro de la POSICIÓN DE LA PLANTA EN EL ACUARIO.
    """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configuramos el formulario
        self.frame = PosicionPlantaAcuarioForm()
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
        self.frame.edit_posicion.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(
            self.frame.edit_posicion, self.frame.text_descripcion
        )


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = PosicionPlantaAcuarioView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
