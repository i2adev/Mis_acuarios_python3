"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      26/11/2025
Comentarios:
    Módulo que contiene el diálogo de la entidad FILTRO.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Dialogs.base_dialog import BaseDialog
from Views.Forms.filtro_form import FiltroForm
from Views.Forms.image_form import ImageForm


class FiltroDialog(BaseDialog):
    """ Diálogo de filtro. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = FiltroForm()
        self.frame_image = ImageForm(self, "FOTOGRAFIAS_FILTRO")
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
        self.frame.combo_tipo_filtro.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.check_termofiltro.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_marca.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_modelo.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_num_serie.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_vol_min_acuario.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_vol_max_acuario.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_consumo_filtro.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_consumo_calentador.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_ancho.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_fondo.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_alto.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_vol_material.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_altura_max_bombeo.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_caudal.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.fecha_compra.edit_date.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.fecha_baja.edit_date.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.edit_motivo_baja.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(self.frame.combo_tipo_filtro,
                         self.frame.check_termofiltro)
        self.setTabOrder(self.frame.check_termofiltro, self.frame.combo_marca)
        self.setTabOrder(self.frame.combo_marca, self.frame.edit_modelo)
        self.setTabOrder(self.frame.edit_modelo, self.frame.edit_num_serie)
        self.setTabOrder(self.frame.edit_num_serie,
                         self.frame.edit_vol_min_acuario)
        self.setTabOrder(self.frame.edit_vol_min_acuario,
                         self.frame.edit_vol_max_acuario)
        self.setTabOrder(self.frame.edit_vol_max_acuario,
                         self.frame.edit_consumo_filtro)
        self.setTabOrder(self.frame.edit_consumo_filtro,
                         self.frame.edit_consumo_calentador)
        self.setTabOrder(self.frame.edit_consumo_calentador,
                         self.frame.edit_ancho)
        self.setTabOrder(self.frame.edit_ancho, self.frame.edit_fondo)
        self.setTabOrder(self.frame.edit_fondo, self.frame.edit_alto)
        self.setTabOrder(self.frame.edit_alto, self.frame.edit_vol_material)
        self.setTabOrder(self.frame.edit_vol_material,
                         self.frame.edit_altura_max_bombeo)
        self.setTabOrder(self.frame.edit_altura_max_bombeo,
                         self.frame.edit_caudal)
        self.setTabOrder(self.frame.edit_caudal,
                         self.frame.fecha_compra.edit_date)
        self.setTabOrder(self.frame.fecha_compra.edit_date,
                         self.frame.fecha_baja.edit_date)
        self.setTabOrder(self.frame.fecha_baja.edit_date,
                         self.frame.edit_motivo_baja)
        self.setTabOrder(self.frame.edit_motivo_baja,
                         self.frame.text_descripcion)


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = FiltroDialog("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
