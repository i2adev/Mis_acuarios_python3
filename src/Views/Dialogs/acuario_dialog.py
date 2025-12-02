"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/08/2025
Comentarios:
    Módulo que contiene el diálogo de la entidad ACUARIO.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Dialogs.base_dialog import BaseDialog
from Views.Forms.acuario_form import AcuarioForm
from Views.Forms.image_form import ImageForm


class AcuarioDialog(BaseDialog):
    """ Diálogo de acuario. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = AcuarioForm()
        self.frame_image = ImageForm(self, "FOTOGRAFIAS_ACUARIO")
        self.frame.setFixedWidth(650)
        self.layout_form_data.addWidget(self.frame)
        self.layout_form_data.addWidget(self.frame_image)
        self.set_tab_order()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las políticas de focus
        self.frame.combo_proyecto.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_nombre_acuario.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.combo_urna.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_tipo_acuario.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_vol_neto.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.fecha_montaje.edit_date.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.fecha_inicio_ciclado.edit_date.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.fecha_fin_ciclado.edit_date.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.fecha_desmontaje.edit_date.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_motivo_desmontaje.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_ubicacion_acuario.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(self.frame.combo_proyecto,
                         self.frame.edit_nombre_acuario)
        self.setTabOrder(self.frame.edit_nombre_acuario, self.frame.combo_urna)
        self.setTabOrder(self.frame.combo_urna, self.frame.combo_tipo_acuario)
        self.setTabOrder(self.frame.combo_tipo_acuario,
                         self.frame.edit_vol_neto)
        self.setTabOrder(self.frame.edit_vol_neto,
                         self.frame.fecha_montaje.edit_date)
        self.setTabOrder(self.frame.fecha_montaje.edit_date,
                         self.frame.fecha_inicio_ciclado.edit_date)
        self.setTabOrder(self.frame.fecha_inicio_ciclado.edit_date,
                         self.frame.fecha_fin_ciclado.edit_date)
        self.setTabOrder(self.frame.fecha_fin_ciclado.edit_date,
                         self.frame.fecha_desmontaje.edit_date)
        self.setTabOrder(self.frame.fecha_desmontaje.edit_date,
                         self.frame.edit_motivo_desmontaje)
        self.setTabOrder(self.frame.edit_motivo_desmontaje,
                         self.frame.edit_ubicacion_acuario)
        self.setTabOrder(self.frame.edit_ubicacion_acuario,
                         self.frame.text_descripcion)


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = AcuarioDialog("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
