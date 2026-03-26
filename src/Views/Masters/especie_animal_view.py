"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      23/03/2026
Comentarios:
    Módulo que contiene el formulario maestro de especie animal.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.Forms.especie_animal_form import EspecieAnimalForm
from Views.Forms.image_form import ImageForm
from Views.Masters.base_view import BaseView


class EspecieAnimalView(BaseView):
    """
    Formulario maestro de la ESPECIE ANIMAL.
    """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configuramos el formulario
        self.frame = EspecieAnimalForm()
        # self.frame.setMinimumWidth(1050)
        self.frame_image = ImageForm(self, "FOTOGRAFIAS_ESPECIE_ANIMAL")
        self.frame_image.setMinimumWidth(800)
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
        self.frame.edit_reino.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_filo.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_clase.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_orden.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_familia.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_genero.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_especie.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_n_comun.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.check_hibrida.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_n_e_hibrida.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_grupo_taxo.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_ph_min.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_ph_max.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_kh_min.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_kh_max.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_gh_min.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_gh_max.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_temp_min.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_temp_max.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_origen.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.edit_tamano.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_comportamiento.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus)
        self.frame.combo_dieta.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.combo_nivel_nado.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.frame.text_descripcion.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Establecer el orden
        self.setTabOrder(self.frame.edit_reino, self.frame.edit_filo)
        self.setTabOrder(self.frame.edit_filo, self.frame.edit_clase)
        self.setTabOrder(self.frame.edit_clase, self.frame.edit_orden)
        self.setTabOrder(self.frame.edit_orden, self.frame.edit_familia)
        self.setTabOrder(self.frame.edit_familia, self.frame.edit_genero)
        self.setTabOrder(self.frame.edit_genero, self.frame.edit_especie)
        self.setTabOrder(self.frame.edit_especie, self.frame.edit_n_comun)
        self.setTabOrder(self.frame.edit_n_comun, self.frame.check_hibrida)
        self.setTabOrder(self.frame.check_hibrida, self.frame.edit_n_e_hibrida)
        self.setTabOrder(self.frame.edit_n_e_hibrida,
                         self.frame.combo_grupo_taxo)
        self.setTabOrder(self.frame.combo_grupo_taxo, self.frame.edit_ph_min)
        self.setTabOrder(self.frame.edit_ph_min, self.frame.edit_ph_max)
        self.setTabOrder(self.frame.edit_ph_max, self.frame.edit_gh_min)
        self.setTabOrder(self.frame.edit_kh_min, self.frame.edit_kh_max)
        self.setTabOrder(self.frame.edit_kh_max, self.frame.edit_gh_min)
        self.setTabOrder(self.frame.edit_gh_min, self.frame.edit_gh_max)
        self.setTabOrder(self.frame.edit_gh_max, self.frame.edit_temp_min)
        self.setTabOrder(self.frame.edit_temp_min, self.frame.edit_temp_max)
        self.setTabOrder(self.frame.edit_temp_max, self.frame.edit_origen)
        self.setTabOrder(self.frame.edit_origen, self.frame.edit_tamano)
        self.setTabOrder(self.frame.edit_tamano,
                         self.frame.combo_comportamiento)
        self.setTabOrder(self.frame.combo_comportamiento,
                         self.frame.combo_dieta)
        self.setTabOrder(self.frame.combo_dieta, self.frame.combo_nivel_nado)
        self.setTabOrder(self.frame.combo_nivel_nado,
                         self.frame.text_descripcion)


# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = EspecieAnimalView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
