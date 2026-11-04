"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      20/10/2026
Comentarios:
    Módulo que contiene la vista de las configuraciones de la aplicación.
"""
import sys

from PyQt6.QtWidgets import QApplication

from Main.Views.base_dialog import BaseDialog
from ModuloConsigfuracion.Views.Forms.configuracion_form import \
    ConfiguracionForm


class ConfiguracionView(BaseDialog):
    """ Formulario de configuración de la aplicación. """

    def __init__(self, w_title: str):
        """ Constructor de clase. """

        super().__init__(w_title)

        # Configuramos los controles
        self.frame = ConfiguracionForm()
        self.frame.setFixedWidth(650)
        self.frame.setFixedHeight(400)
        self.layout_form_data.addWidget(self.frame)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = ConfiguracionView("...::OOO::....")

    # Cargar el archivo .qss
    with open("../../../Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
