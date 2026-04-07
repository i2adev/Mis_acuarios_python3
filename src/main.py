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
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox

from Controllers.login_controller import LoginDialogController
from Controllers.main_view_controller import MainViewController
from Model.DAO.base_dao import BaseDAO
from Model.DAO.usuario_dao import UsuarioDAO
from Model.Entities.usuario_entity import UsuarioEntity
from Views.Dialogs.login_dialog import LoginDialog
import os
import globals

# Versión del programa
__version__ = "0.39.0"


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

    # ELimina la característica de DirectDraw en windows
    os.environ["QT_QPA_PLATFORM"] = "windows:nodirectwrite"

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

    # Mostramos las rutas de los recursos
    print("\nRutas de recursos:")
    print(f"✅ {globals.PATH_RESOURCES}")
    print(f"✅ {globals.PATH_IMAGES}")
    print(f"✅ {globals.PATH_FONTS}")
    print(f"✅ {globals.PATH_STYLES}")
    print(f"✅ {globals.PATH_STYLES}")
    print()

    # Carga las fuentes desde el recurso
    _ = load_directory_fonts(globals.PATH_FONTS)

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


def load_directory_fonts(dir_path: str) -> list:
    directory = Path(dir_path)
    loaded_fonts = []

    # 1. Verificar si la carpeta existe para evitar errores previos
    if not directory.exists():
        print(f"⚠️ La carpeta no existe: {dir_path}")
        return []

    print("Tipos de letra cargados:")
    # Carga las fuentes del directorio
    for file in directory.glob("*.[to]tf"):
        # 2. Usar resolve() para enviar la ruta absoluta completa y evitar fallos de lectura
        absolute_path = str(file.resolve())
        font_id = QFontDatabase.addApplicationFont(absolute_path)

        if font_id != -1:
            families = QFontDatabase.applicationFontFamilies(font_id)
            if families:
                family = families[0]
                loaded_fonts.append(family)
                print(f"✅ Fuente cargada: {family}")
        else:
            # Si el error persiste aquí, el archivo .ttf está corrupto o bloqueado
            print(f"❌ Error al cargar: {file.name}")

    # 3. Devuelve la lista de fuentes
    return loaded_fonts


if __name__ == "__main__":
    main()
