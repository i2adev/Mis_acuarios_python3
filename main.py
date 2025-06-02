"""
Punto de entrada de la aplicación
"""
# Importaciones
import sys
from PyQt6.QtWidgets import QApplication
from Controllers.tipo_filtro_controller import Tipo_filtro_controller

# Entrada al programa
def main():
    """ Punto de entrada a la aplicación """
    app = QApplication(sys.argv)

    # Cargar el archivo .qss
    with open("Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        testily = f.read()
        app.setStyleSheet(testily)

    ctrl = Tipo_filtro_controller()
    ctrl.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


