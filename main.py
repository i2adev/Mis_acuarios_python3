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
from PyQt6.QtWidgets import QApplication, QMessageBox
from Controllers.main_view_controller import MainViewController

# Versión del programa
__version__ = "0.7.1"

from Model.DAO.base_dao import BaseDAO

from Views.main_view import MainView


# Entrada al programa
def main():
    """ Punto de entrada a la aplicación """
    app = QApplication(sys.argv)

    # Cargar el archivo .qss
    with open("Resources/Styles/main_style.qss", "r",
              encoding="utf-8-sig") as f:
        testily = f.read()
        app.setStyleSheet(testily)

    # # Limpia la base de datos
    # msg = BaseDAO.clean_database()
    # if msg.is_success:
    #     QMessageBox.information(
    #         None,
    #         "LIMPIEZA DE BASE DE DATOS",
    #         msg.value
    #     )
    # else:
    #     QMessageBox.warning(
    #         None,
    #         "LIMPIEZA DE BASE DE DATOS",
    #         msg.error_msg
    #     )

    # # Se implementa la copia de la base de datos a fiche sql
    # origen = str(Path(__file__).resolve().parent /
    #         "Services" / "Database" / "MISACUARIOS.sqlite3")
    #
    # destino = str(Path(__file__).resolve().parent /
    #         "Services" / "Database" / "Backup.sql")
    #
    # if BaseDAO.export_db_sql(origen, destino):
    #     QMessageBox.information(
    #         None,
    #         "BACKUP DE LA BASE DE DATOS",
    #         f"""
    #         SE HA COPIADO LA ESTRUCTURA Y LOS DATOS DE LA BASE DE DATOS:
    #         - ORIGEN:   {origen}
    #         - DESTINO:  {destino}
    #         """
    #     )
    # else:
    #     QMessageBox.warning(
    #         None,
    #         "BACKUP DE LA BASE DE DATOS",
    #         "NO SE HA PODIDO REALIZAR EL BACKUP"
    #     )

    ctrl = MainViewController()
    ctrl.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


