"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Commentarios:
    Fichero que contiene el método main(), que es la entrada al
    programa. Este método da estilo a la aplicación y abre la ventana
    principal.
"""

# Importaciones
import sys
from PyQt6.QtWidgets import QApplication
from Controllers.tipo_filtro_controller import TipoFiltroController

# Versión del programa
__version = "0.0.2"

# Entrada al programa
def main():
    """ Punto de entrada a la aplicación """
    app = QApplication(sys.argv)

    # Cargar el archivo .qss
    with open("Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        testily = f.read()
        app.setStyleSheet(testily)

    ctrl = TipoFiltroController()
    ctrl.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


