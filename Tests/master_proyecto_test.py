"""
TESTS PARA EL FORMULARIO MAESTRO DE PROYECTO
"""
import pytest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

from Model.DAO.proyecto_dao import ProyectoDAO
from Views.Masters.proyecto_view import ProyectoView
from Model.Entities.proyecto_entity import ProyectoEntity
from Controllers.proyecto_master_controller import ProyectoMasterController


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
