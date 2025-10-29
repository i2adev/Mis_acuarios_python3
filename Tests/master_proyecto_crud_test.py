import pytest
from PyQt6.QtCore import Qt

from Controllers.proyecto_master_controller import ProyectoMasterController
from Model.DAO.proyecto_dao import ProyectoDAO
from Model.Entities.proyecto_entity import ProyectoEntity
from Views.Masters.proyecto_view import ProyectoView


@pytest.fixture
def app(qtbot):
    """Crea una instancia completa del formulario maestro de proyecto."""
    # Crear componentes MVC
    view = ProyectoView("TESTS DEL MAESTRO DE PROYECTO")
    dao = ProyectoDAO()
    entity = ProyectoEntity()
    controller = ProyectoMasterController(view, dao, entity)

    # Registrar la vista para control de pytest-qt
    qtbot.addWidget(view)
    view.show()

    # Devolver ambos si se quiere probar interacciones complejas
    return view, controller


def test_proyecto_insertion(qtbot, app):
    """Ejemplo: escribir en el QLineEdit y verificar."""
    view, controller = app

    # Mostrar y activar ventana
    view.show()
    qtbot.waitExposed(view)
    view.activateWindow()
    view.raise_()

    # Asegurar foco y simular escritura
    qtbot.mouseClick(view.frame.edit_nombre_proyecto, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(view.frame.edit_nombre_proyecto, "Mi acuario de discos")

    # qtbot.mouseClick(view.frame.combo_estado_proyecto,
    #                  Qt.MouseButton.LeftButton)
    # qtbot.keyClicks(view.frame.combo_estado_proyecto, "En curso")
    # qtbot.keyClick(view.frame.combo_estado_proyecto, Qt.Key.Key_Return)

    view.frame.combo_estado_proyecto.setCurrentIndex(
        view.frame.combo_estado_proyecto.findText("En curso")
    )

    qtbot.mouseClick(view.frame.date_inicio.edit_date,
                     Qt.MouseButton.LeftButton)
    qtbot.keyClicks(view.frame.date_inicio.edit_date, "14/06/2024")

    qtbot.mouseClick(view.frame.edit_motivo_cierre, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(view.frame.edit_motivo_cierre, "Mudanza de casa.")

    view.frame.text_descripcion.setPlainText(
        "Proyecto iniciado por la pasión que siento por los peces disco. "
        "Se inicia el proyecto en base a un acuario Eheim Incpiria 330."
    )

    qtbot.wait(1000)
    assert view.frame.edit_nombre_proyecto.text() == "Mi acuario de discos"


def test_proyecto_insert(qtbot, app):
    view, controller = app

    # Mostrar y activar ventana
    view.show()
    qtbot.waitExposed(view)
    view.activateWindow()
    view.raise_()

    # Casop 1: Insertar todos los campos
    ## Rellenar formulario
    qtbot.mouseClick(view.frame.edit_nombre_proyecto, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(view.frame.edit_nombre_proyecto, "Mi acuario de discos")

    view.frame.combo_estado_proyecto.setCurrentIndex(
        view.frame.combo_estado_proyecto.findText("En curso")
    )

    qtbot.mouseClick(view.frame.date_inicio.edit_date,
                     Qt.MouseButton.LeftButton)
    qtbot.keyClicks(view.frame.date_inicio.edit_date, "14/06/2024")

    qtbot.mouseClick(view.frame.date_fin.edit_date, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(view.frame.date_fin.edit_date, "29/10/2025")

    qtbot.mouseClick(view.frame.edit_motivo_cierre, Qt.MouseButton.LeftButton)
    qtbot.keyClicks(view.frame.edit_motivo_cierre, "Mudanza de casa.")

    view.frame.text_descripcion.setPlainText(
        "Proyecto iniciado por la pasión que siento por los peces disco. "
        "Se inicia el proyecto en base a un acuario Eheim Incpiria 330."
    )

    qtbot.wait(1000)
    # qtbot.mouseClick(view.button_insert, Qt.MouseButton.LeftButton)

    # Ningún QMessageBox se muestra
    assert view.frame.edit_nombre_proyecto.text() == "Mi acuario de discos"
