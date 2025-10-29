"""
TESTS PARA EL FORMULARIO MAESTRO DE PROYECTO
"""
import sys
from pathlib import Path

import pytest

# Añade la raíz del proyecto al sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Model.DAO.proyecto_dao import ProyectoDAO
from Services.Validators.proyecto_validator import ProyectoValidator
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


def test_validator_nombre_proyecto(qtbot, app):
    """Prueba de validación del nombre del proyecto."""
    view, controller = app
    validator = ProyectoValidator()

    # Caso 1: Insertar nombre de proyecto vacío
    view.frame.edit_nombre_proyecto.setText("")
    resultado = validator.validate_nombre_proyecto(
        view.frame.edit_nombre_proyecto)
    assert resultado.value == None

    # Caso 2: Nombre demasiado largo
    view.frame.edit_nombre_proyecto.clear()
    view.frame.edit_nombre_proyecto.setFocus()
    view.frame.edit_nombre_proyecto.setFocus()
    texto = (
        "Mis acuarios del tipo de prueba de proyección internacional de las "
        "naciones del mundo del acuariófilo de la nación correspondiente al "
        "artículo 450 de los estatutos de la sociedad acuariofila social de "
        "no se qué."
    )

    view.frame.edit_nombre_proyecto.setText(texto)
    resultado = validator.validate_nombre_proyecto(
        view.frame.edit_nombre_proyecto)
    assert resultado.value == None

    # Caso 3: Nombre válido
    view.frame.edit_nombre_proyecto.clear()
    view.frame.edit_nombre_proyecto.setFocus()
    texto = "Mis acuarios"
    view.frame.edit_nombre_proyecto.setText(texto)
    resultado = validator.validate_nombre_proyecto(
        view.frame.edit_nombre_proyecto)
    assert resultado.value == 1


def test_validator_fecha_inicio(qtbot, app):
    """Prueba la validación de la fecha de inicio del proyecto."""
    view, controller = app
    validator = ProyectoValidator()

    # Caso 1: Dejar la fecha de inicio vacía
    view.frame.date_inicio.clear_date()
    resultado = validator.validate_fecha_inicio(view.frame.date_inicio)
    assert resultado.value == None


def test_validator_motivo_cierre(qtbot, app):
    """Prueba de valicación de motivo cierre del proyecto."""
    view, controller = app
    validator = ProyectoValidator()

    # Caso 1: Motivo de cierre nulo
    view.frame.edit_motivo_cierre.setText("")
    resultado = validator.validate_motivo_cierre(view.frame.edit_motivo_cierre)
    assert resultado.value == 1

    # Caso 2: Sobrepaso de la longitud de campo
    view.frame.edit_motivo_cierre.clear()
    view.frame.edit_motivo_cierre.setFocus()
    view.frame.edit_motivo_cierre.setText(
        "Lorem Ipsum es simplemente el texto de relleno de las imprentas y "
        "archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de "
        "las industrias desde el año 1500, cuando un impresor (N. del T. persona"
        " que se dedica a la imprenta) desconocido usó una galería de textos "
        "y los mezcló de tal manera que logró hacer un libro de textos "
        "especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como "
        "texto de relleno en documentos electrónicos, quedando esencialmente "
        "igual al original. Fue popularizado en los 60s con la creación de las "
        "hojas 'Letraset', las cuales contenian pasajes de Lorem Ipsum, y más "
        "recientemente con software de autoedición, como por ejemplo Aldus "
        "PageMaker, el cual incluye versiones de Lorem Ipsum."
    )
    resultado = validator.validate_motivo_cierre(view.frame.edit_motivo_cierre)
    assert resultado.value == None

    # Caso 3: Uso correcto del campo
    view.frame.edit_motivo_cierre.clear()
    view.frame.edit_motivo_cierre.setFocus()
    view.frame.edit_motivo_cierre.setText("Por motivos de mudanza.")
    resultado = validator.validate_motivo_cierre(view.frame.edit_motivo_cierre)
    assert resultado.value == 1
