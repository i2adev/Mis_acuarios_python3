"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/03/2026
Comentarios:
    Módulo que contiene el diálogo de la entidad POSICIÓN DE LA PLANTA EN EL 
    ACUARIO.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Dialogs.base_dialog import BaseDialog
from Views.Forms.posicion_planta_Acuario_form import PosicionPlantaAcuarioForm


class PosicionPlantaAcuarioDialog(BaseDialog):
    """ Diálogo de la posición de la planta en el acuario.. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = PosicionPlantaAcuarioForm()
        self.frame.setFixedWidth(450)
        self.layout_form_data.addWidget(self.frame)
        self.set_tab_order()

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

    ventana = PosicionPlantaAcuarioDialog("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
