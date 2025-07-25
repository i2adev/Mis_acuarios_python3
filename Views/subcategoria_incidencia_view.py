"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      25/07/2025
Commentarios:
    Módulo que contiene el formulario maestro de la subcategoría de
    incidencia.
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from Views.base_view import BaseView
from Views.subcategoria_incidencia_form import SubcategoriaIncidenciaForm


class SubcategoriaIncidenciaView(BaseView):
    """
    Formulario maestro de la SUBCATEGORÍA DE INCIDENCIA.
    """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configuramos el formulario
        self.frame = SubcategoriaIncidenciaForm()
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
        self.frame.combo_categoria_incidencia.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus
        )
        self.frame.edit_subcategoria_incidencia.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus
        )
        self.frame.text_observaciones.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus
        )

        # Establecer el orden
        self.setTabOrder(
            self.frame.combo_categoria_incidencia,
            self.frame.edit_subcategoria_incidencia
        )
        self.setTabOrder(
            self.frame.edit_subcategoria_incidencia,
            self.frame.text_observaciones
        )

# Entrada a la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = SubcategoriaIncidenciaView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())