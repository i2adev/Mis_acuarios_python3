"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      17/09/2026
Comentarios:
    Módulo que contiene el diálogo de la entidad CONTROLADOR DE
    TEMPERATURA.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Main.Views.base_dialog import BaseDialog
from ModuloMaestro.Views.Forms.controlador_temperatura_form import \
    ControladorTemperaturaForm
from ModuloMaestro.Views.Forms.image_form import ImageForm


class ControladorTemperaturaDialog(BaseDialog):
    """ Diálogo de equipamiento. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = ControladorTemperaturaForm()
        self.frame_image = ImageForm(
            self, "FOTOGRAFIAS_CONTROLADOR_TTEMPERATURA")
        self.frame_image.setFixedWidth(550)
        self.layout_form_data.addWidget(self.frame)
        self.layout_form_data.addWidget(self.frame_image)
        self.set_tab_order()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las políticas de focus
        self.frame.combo_tipo_controlador.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.combo_marca.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_modelo.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_num_serie.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_temperatura_minima.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_temperatura_maxima.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_consumo.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.fecha_alta.edit_date.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.fecha_baja.edit_date.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_motivo_baja.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(self.frame.combo_tipo_controlador,
                         self.frame.combo_marca)
        self.setTabOrder(self.frame.combo_marca,
                         self.frame.edit_modelo)
        self.setTabOrder(self.frame.edit_modelo,
                         self.frame.edit_num_serie)
        self.setTabOrder(self.frame.edit_num_serie,
                         self.frame.edit_temperatura_minima)
        self.setTabOrder(self.frame.edit_temperatura_minima,
                         self.frame.edit_temperatura_maxima)
        self.setTabOrder(self.frame.edit_temperatura_maxima,
                         self.frame.edit_consumo)
        self.setTabOrder(self.frame.edit_consumo,
                         self.frame.fecha_alta.edit_date)
        self.setTabOrder(self.frame.fecha_alta.edit_date,
                         self.frame.fecha_baja.edit_date)
        self.setTabOrder(self.frame.fecha_baja.edit_date,
                         self.frame.edit_motivo_baja)
        self.setTabOrder(self.frame.edit_motivo_baja,
                         self.frame.text_descripcion)


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ControladorTemperaturaDialog("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
