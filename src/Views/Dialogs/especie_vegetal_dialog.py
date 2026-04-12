"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      09/04/2026
Comentarios:
    Módulo que contiene el diálogo de la entidad ESPECIE VEGETAL.
"""

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QSizePolicy, QSpacerItem, \
    QVBoxLayout, QWidget
from Views.Dialogs.base_dialog import BaseDialog
from Views.Forms.especie_vegetal_form import EspecieVegetalForm
from Views.Forms.image_form import ImageForm


class EspecieVegetalDialog(BaseDialog):
    """ Diálogo de especie animal. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configura el formulario
        self.frame = EspecieVegetalForm()

        self.frame_image = ImageForm(self, "FOTOGRAFIAS_ESPECIE_VEGETAL")
        self.frame_image.setMinimumWidth(800)

        # self.frame.setFixedWidth(650)
        self.layout_form_data.addWidget(self.frame)
        self.layout_form_data.addWidget(self.frame_image)
        self.set_tab_order()

    def set_tab_order(self):
        """ Establece el orden de tabulación de los controles. """

        # Eliminar el focus de los widgets que no lo necesitan
        for widget in self.findChildren(QWidget):
            widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Establecemos las políticas de focus
        self.frame.edit_reino.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_división.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_clase.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_orden.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_familia.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_genero.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_especie.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_n_comun.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_ph_min.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_ph_max.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_kh_min.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_kh_max.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_gh_min.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_gh_max.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_temp_min.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_temp_max.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_origen.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_posicion.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.combo_req_iluminacion.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.combo_req_co2.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_crecimiento.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_dificultad.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(self.frame.edit_reino, self.frame.edit_división)
        self.setTabOrder(self.frame.edit_división, self.frame.edit_clase)
        self.setTabOrder(self.frame.edit_clase, self.frame.edit_orden)
        self.setTabOrder(self.frame.edit_orden, self.frame.edit_familia)
        self.setTabOrder(self.frame.edit_familia, self.frame.edit_genero)
        self.setTabOrder(self.frame.edit_genero, self.frame.edit_especie)
        self.setTabOrder(self.frame.edit_especie, self.frame.edit_n_comun)
        self.setTabOrder(self.frame.edit_n_comun, self.frame.edit_ph_min)
        self.setTabOrder(self.frame.edit_ph_min, self.frame.edit_ph_max)
        self.setTabOrder(self.frame.edit_ph_max, self.frame.edit_gh_min)
        self.setTabOrder(self.frame.edit_kh_min, self.frame.edit_kh_max)
        self.setTabOrder(self.frame.edit_kh_max, self.frame.edit_gh_min)
        self.setTabOrder(self.frame.edit_gh_min, self.frame.edit_gh_max)
        self.setTabOrder(self.frame.edit_gh_max, self.frame.edit_temp_min)
        self.setTabOrder(self.frame.edit_temp_min, self.frame.edit_temp_max)
        self.setTabOrder(self.frame.edit_temp_max, self.frame.edit_origen)
        self.setTabOrder(self.frame.edit_origen, self.frame.combo_posicion)
        self.setTabOrder(self.frame.combo_posicion,
                         self.frame.combo_req_iluminacion)
        self.setTabOrder(self.frame.combo_req_iluminacion,
                         self.frame.combo_req_co2)
        self.setTabOrder(self.frame.combo_req_co2,
                         self.frame.combo_crecimiento)
        self.setTabOrder(self.frame.combo_crecimiento,
                         self.frame.combo_dificultad)
        self.setTabOrder(self.frame.combo_dificultad,
                         self.frame.text_descripcion)


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = EspecieVegetalDialog("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
