"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      02/06/2025
Comentarios:
    Fichero que contiene el método main(), que es la entrada al
    programa. Este método da estilo a la aplicación y abre la ventana
    principal.
"""

import sys
import traceback
from pathlib import Path

from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QApplication, QDialog

from Controllers.login_controller import LoginDialogController
from Controllers.main_view_controller import MainViewController
from Model.DAO.usuario_dao import UsuarioDAO
from Model.Entities.usuario_entity import UsuarioEntity
from Views.Dialogs.login_dialog import LoginDialog

# Versión del programa
__version__ = "0.16.0"


def excepthook(exc_type, exc_value, exc_traceback):
    """
    Muestra en consola cualquier excepción no capturada,
    incluso las que ocurren dentro del event loop de Qt.
    """
    print(
        "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    )
    sys.exit(1)


sys.excepthook = excepthook


# Entrada al programa
def main():
    """ Punto de entrada a la aplicación """

    app = QApplication(sys.argv)

    def resource_path(relative_path):
        """Devuelve la ruta absoluta al recurso, compatible con PyInstaller."""
        base_path = getattr(sys, '_MEIPASS', Path(__file__).parent)
        return Path(base_path) / relative_path

    # Cargar el estilo
    qss_path = resource_path("Resources/Styles/main_style.qss")
    with open(qss_path, "r", encoding="utf-8") as f:
        style = f.read()
        app.setStyleSheet(style)

    # Carga las fuentes desde el recurso
    QFontDatabase.addApplicationFont(":/Fonts/Roboto-Bold.ttf")
    QFontDatabase.addApplicationFont(":/Fonts/Roboto-Medium.ttf")
    QFontDatabase.addApplicationFont(":/Fonts/Roboto-Regular.ttf")
    QFontDatabase.addApplicationFont(":/Fonts/Roboto-Medium.ttf")

    # # Limpia la base de datos
    # msg = BaseDAO.clean_database()
    # if msg.is_success:
    #     res = BaseDAO.fill_essential_info()
    #     if not res.is_success:
    #         QMessageBox.information(
    #             None,
    #             "LIMPIEZA DE BASE DE DATOS",
    #             res.error_msg
    #         )
    #         return
    #
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

    # Arranque inicial
    view = LoginDialog()
    dao = UsuarioDAO()
    mod = UsuarioEntity()
    ctrl = LoginDialogController(view, dao, mod)
    res = ctrl.show_modal()

    if res == QDialog.DialogCode.Accepted:
        # Abrir la ventana principal
        ctrl = MainViewController()
        ctrl.show()
        sys.exit(app.exec())
    else:
        # Cancelado → salir de la aplicación
        sys.exit(0)


if __name__ == "__main__":
    main()
