"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  11/11/2025
Comentarios:
    Controlador base de acuario.
"""
from PyQt6.QtCore import QDate, QDateTime, QTime
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMessageBox, QPushButton, QColorDialog

import globals
from Controllers.base_controller import BaseController
from Controllers.tipo_acuario_dialog_controller import \
    TipoAcuarioDialogController
from Controllers.urna_dialog_controller import UrnaDialogController
from Model.DAO.acuario_dao import AcuarioDAO
from Model.DAO.proyecto_dao import ProyectoDAO
from Model.DAO.tipo_acuario_dao import TipoAcuarioDAO
from Model.DAO.urna_dao import UrnaDAO
from Model.Entities.acuario_entity import AcuarioEntity
from Model.Entities.tipo_acuario_entity import TipoAcuarioEntity
from Model.Entities.urna_entity import UrnaEntity
from Services.Result.result import Result
from Services.Validators.acuario_validator import AcuarioValidator
from Views.Dialogs.acuario_dialog import AcuarioDialog
from Views.Dialogs.tipo_acuario_dialog import TipoAcuarioDialog
from Views.Dialogs.urna_dialog import UrnaDialog
from Views.Masters.acuario_view import AcuarioView


class AcuarioController(BaseController):
    """ 
    Controlador base del cuadro de diálogo y formulario maestro de proyecto. 
    """

    def __init__(self, view: AcuarioDialog | AcuarioView,
                 dao: AcuarioDAO,
                 model: AcuarioEntity):
        """
        Inicializa el controlador de la urna.
        :param view: AcuarioDialog | AcuarioView
        :param dao: AcuarioDAO
        :param model: AcuarioEntity
        """

        # Atributos
        self._acuario_result = None

        # Llamaos al constructor de la superclase
        super().__init__(view, dao, model)

        # Llenamos los combos
        self._fill_combos()

    def _entity_configuration(self) -> AcuarioEntity:
        """ Configura la entidad. """

        ent = AcuarioEntity()

        if self._view.frame.edit_id.text():
            ent.id = int(self._view.frame.edit_id.text())
        else:
            ent.id = None

        ent.id_proyecto = int(self._view.frame.combo_proyecto.currentData())

        if self._view.frame.edit_cod_color.text():
            ent.cod_color = self._view.frame.edit_cod_color.text()
        else:
            ent.cod_color = None

        ent.nombre = self._view.frame.edit_nombre_acuario.text()
        ent.id_urna = int(self._view.frame.combo_urna.currentData())
        ent.id_tipo = int(self._view.frame.combo_tipo_acuario.currentData())

        if self._view.frame.edit_vol_neto.text():
            ent.volumen_neto = self._view.frame.edit_vol_neto.text()
        else:
            ent.volumen_neto = None

        if self._view.frame.edit_cod_color.text():
            ent.cod_color = self._view.frame.edit_cod_color.text()
        else:
            ent.cod_color = None

        montaje = self._view.frame.fecha_montaje.date()
        if montaje.isValid():
            time_inicio = QDateTime(montaje, QTime(0, 0))
            ent.fecha_montaje = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_montaje = None

        inicio_ciclado = self._view.frame.fecha_inicio_ciclado.date()
        if inicio_ciclado.isValid():
            time_inicio = QDateTime(inicio_ciclado, QTime(0, 0))
            ent.fecha_inicio_ciclado = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_inicio_ciclado = None

        fin_ciclado = self._view.frame.fecha_fin_ciclado.date()
        if fin_ciclado.isValid():
            time_inicio = QDateTime(fin_ciclado, QTime(0, 0))
            ent.fecha_fin_ciclado = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_fin_ciclado = None

        desmontaje = self._view.frame.fecha_desmontaje.date()
        if desmontaje.isValid():
            time_inicio = QDateTime(desmontaje, QTime(0, 0))
            ent.fecha_desmontaje = int(time_inicio.toSecsSinceEpoch())
        else:
            ent.fecha_desmontaje = None

        if self._view.frame.edit_motivo_desmontaje.text():
            ent.motivo_desmontaje = self._view.frame.edit_motivo_desmontaje.text()
        else:
            ent.motivo_desmontaje = None

        if self._view.frame.edit_ubicacion_acuario.text():
            ent.ubicacion_acuario = self._view.frame.edit_ubicacion_acuario.text()
        else:
            ent.ubicacion_acuario = None

        if self._view.frame.text_descripcion.toPlainText():
            ent.descripcion = self._view.frame.text_descripcion.toPlainText()
        else:
            ent.descripcion = None

        return ent

    # INICIO DE CRUD ---------------------------------------------------
    def _insert(self) -> Result:
        """ Inserta un registro en la base de datos. """

        # Validamos el formulario
        val = self._validate_view()

        if not val.is_success:
            return val

        # Configura la entidad
        ent = self._entity_configuration()

        # Inserta el registro
        res_acuario = self._dao.insert(ent)
        if not res_acuario.is_success:
            return res_acuario

        # Insertamos las fotografías
        res_foto = self._view.frame_image.insert_images(res_acuario.value)
        if not res_foto.is_success:
            return res_foto

        return Result.success(res_acuario.value)

    def _update(self) -> Result:
        """ Actualiza el registro en la base de datos. """

        # Valida el formulario
        val = self._validate_view(False, False)

        if not val.is_success:
            return val

        # Configura la entidad
        ent = self._entity_configuration()

        # Actualiza el registro
        res_acuario = self._dao.update(ent)

        if not res_acuario.is_success:
            return res_acuario

        # Actualizamos las fotografías
        res_foto = self._view.frame_image.insert_images(res_acuario.value)
        if not res_foto.is_success:
            return res_foto

        return Result.success(ent.id)

    def _delete(self, ide: int) -> Result:
        """
        Elimina un registro de la base de datos.
        :param ide: Id del registro a eliminar.
        """

        # Solicitamos doble confirmación
        res = QMessageBox.question(
            self._view,
            self._view.window_title,
            "¿ESTÁS SEGURO QUE DESEAS ELIMINAR EL REGISTRO?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if res == QMessageBox.StandardButton.No:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "NO SE ELIMINARÁ EL REGISTRO"
            )
            return Result.success(0)

        res = QMessageBox.question(
            self._view,
            self._view.window_title,
            "R E P I T O\n¿ESTÁS SEGURO QUE DESEAS ELIMINAR EL REGISTRO?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if res == QMessageBox.StandardButton.No:
            QMessageBox.information(
                self._view,
                self._view.window_title,
                "NO SE ELIMINARÁ EL REGISTRO"
            )
            return Result.success(0)

        # Elimina el registro
        res = self._dao.delete(ide)

        if not res.is_success:
            return Result.failure(res.error_msg)

        return Result.success(ide)

    # FIN DE CRUD --------------------------------------------------

    def _validate_view(self, val_color: bool = True,
                       val_is_mounted: bool = True) -> Result:
        """
        Valida el formulario.
        :param val_color: Indica si valida el color.
        :param val_is_mounted: Indica si valida si la urna está montada.
        """

        # Valida el color
        res = AcuarioValidator.validate_color(
            self._view.frame.edit_cod_color,
            int(self._view.frame.combo_proyecto.currentData()),
            val_color
        )

        if not res.is_success:
            self._view.frame.combo_proyecto.setFocus()
            return res

        # Valida el proyecto
        res = AcuarioValidator.validate_proyecto(
            self._view.frame.combo_proyecto
        )

        if not res.is_success:
            self._view.frame.combo_proyecto.setFocus()
            return res

        # Valida el nombre del acuario
        res = AcuarioValidator.validate_nombre(
            self._view.frame.edit_nombre_acuario
        )

        if not res.is_success:
            self._view.frame.edit_nombre_acuario.setFocus()
            return res

        # Valida la urna
        res = AcuarioValidator.validate_urna(
            self._view.frame.combo_urna, val_is_mounted
        )

        if not res.is_success:
            self._view.frame.combo_urna.setFocus()
            return res

        # Valida el tipo de acuario
        res = AcuarioValidator.validate_tipo_acuario(
            self._view.frame.combo_tipo_acuario
        )

        if not res.is_success:
            self._view.frame.combo_tipo_acuario.setFocus()
            return res

        # Valida el volumen neto
        res = AcuarioValidator.validate_vol_neto(
            self._view.frame.edit_vol_neto
        )

        if not res.is_success:
            self._view.frame.edit_vol_neto.setFocus()
            return res

        # Valida la fecha de montaje
        res = AcuarioValidator.validate_fecha_montaje(
            self._view.frame.fecha_montaje
        )

        if not res.is_success:
            self._view.frame.fecha_montaje.edit_date.setFocus()
            return res

        # Valida el motivo de desmontaje
        res = AcuarioValidator.validate_motivo_desmontaje(
            self._view.frame.edit_motivo_desmontaje
        )

        if not res.is_success:
            self._view.frame.edit_fecha_montaje.setFocus()
            return res

        # Valida la ubicación del acuario
        res = AcuarioValidator.validate_ubicación_acuarfio(
            self._view.frame.edit_ubicacion_acuario
        )

        if not res.is_success:
            self._view.frame.edit_ubicacion_acuario.setFocus()
            return res

        return Result.success(1)

    def _get_row_id(self, sender: QPushButton | QAction) -> Result:
        """ Obtiene el ID del registro seleccionado."""

        control = type(sender).__name__

        if control == "QPushButton":
            # Sí tenemos un registro cargado
            if not self._view.frame.edit_id.text():
                return Result.failure("DEBES SELECCIONAR UN REGISTRO DE LA "
                                      "TABLA.")

            # Obtener el ID desde el cuadro de texto id_parent
            id_row = int(self._view.frame.edit_id.text())
            return Result.success(id_row)
        elif control == "QAction":
            # Carga el modelo de la fila seleccionada
            selection_model = self._view.data_table.selectionModel()

            # Chequea si se ha seleccionado una fila
            if not selection_model.hasSelection():
                return Result.failure("DEBES PULSAR SOBRE UN REGISTRO.")

            # Configuramos la fila
            index = selection_model.currentIndex()
            fila = index.row()
            modelo = self._view.data_table.model()

            # Lee los datos del modelo
            id_row = modelo.index(fila, 0).data()
            return Result.success(id_row)
        else:
            return Result.failure("DEBE SELECCIONAR O CARGAR UN REGISTRO")

    def _get_acuario(self):
        """ Devuelve el acuario resultante. """

        return self._acuario_result

    def _load_record(self):
        """ Carga el registro en el formulario. """

        # Carga los datos del registro
        res_id = self._load_data()

        # Carga las imágenes
        self._view.frame_image.load_images(res_id.value)

    def _fill_combos(self):
        """ Llena los combos del formulario"""

        self._fill_combo_urna()
        self._fill_combo_tipo_acuario()
        self._fill_combo_proyecto()

    def _fill_combo_proyecto(self):
        """ Llena el combo de los proyectos. """

        # Vaciamos el combo
        self._view.frame.combo_proyecto.clear()

        # Obtenemos los datos
        dao = ProyectoDAO()
        lista = dao.get_list_combo_by_user(globals.CURRENT_USER.id)

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LAS 'URNAS'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_proyecto.addItem(
                ent.nombre, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_proyecto)

        # Deseleccionamos el valor
        self._view.frame.combo_proyecto.setCurrentIndex(-1)

    def _fill_combo_urna(self):
        """ Llena el combo de la urna. """

        # Vaciamos el combo
        self._view.frame.combo_urna.clear()

        # Obtenemos los datos
        dao = UrnaDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LAS 'URNAS'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_urna.addItem(
                ent.modelo, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_urna)

        # Deseleccionamos el valor
        self._view.frame.combo_urna.setCurrentIndex(-1)

    def _fill_combo_tipo_acuario(self):
        """ Llena el combo del tipo de acuario. """

        # Vaciamos el combo
        self._view.frame.combo_tipo_acuario.clear()

        # Obtenemos los datos
        dao = TipoAcuarioDAO()
        lista = dao.get_list_combo()

        if not lista.is_success:
            return Result.failure(
                "NO SE HAN PODIDO OBTENER LOS 'TIPOS DE ACUARIO'."
            )

        # Llenamos el combo
        for ent in lista.value:
            self._view.frame.combo_tipo_acuario.addItem(
                ent.observaciones, ent.id
            )

        # Establecemos el autocompletado
        self._set_autocomplete(self._view.frame.combo_tipo_acuario)

        # Deseleccionamos el valor
        self._view.frame.combo_tipo_acuario.setCurrentIndex(-1)

    def _open_urna_dialog(self):
        """ Abrimos el diálogo de la urna. """

        # Configuramos el CONTROLADOR
        view = UrnaDialog("INSERTAR URNA")
        dao = UrnaDAO()
        mod = UrnaEntity()

        ctrl = UrnaDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_urna

        self._fill_combo_urna()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_tipo_acuario_dialog(self):
        """ Abrimos el diálogo del tipo de acuario. """

        # Configuramos el CONTROLADOR
        view = TipoAcuarioDialog("INSERTAR URNA")
        dao = TipoAcuarioDAO()
        mod = TipoAcuarioEntity()

        ctrl = TipoAcuarioDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_tipo_acuario

        self._fill_combo_urna()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _load_data(self) -> Result:
        """ Carga los datos. """

        # Carga el modelo de la fila seleccionada
        selection_model = self._view.data_table.selectionModel()

        # Chequea si se ha seleccionado una fila
        if not selection_model.hasSelection():
            return Result.failure(
                "ANTES DE CARGAR UN REGISTRO, DEBES "
                "SELECCIONAR UNO EN LA TABLA."
            )

        # Configuramos la fila
        index = selection_model.currentIndex()
        fila = index.row()
        modelo = self._view.data_table.model()

        # Lee los datos del modelo
        id_ent = modelo.index(fila, 0).data()
        proyecto = modelo.index(fila, 2).data()
        cod_color = modelo.index(fila, 3).data()
        nombre = modelo.index(fila, 4).data()
        urna = modelo.index(fila, 5).data()
        tipo = modelo.index(fila, 6).data()
        volumen = self.brakdown_volumes(modelo.index(fila, 7).data())
        fecha_montaje = QDate.fromString(
            str(modelo.index(fila, 8).data()), "dd/MM/yyyy")
        fecha_inicio_ciclado = QDate.fromString(
            str(modelo.index(fila, 9).data()), "dd/MM/yyyy")
        fecha_fin_ciclado = QDate.fromString(
            str(modelo.index(fila, 10).data()), "dd/MM/yyyy")
        ubicacion = modelo.index(fila, 12).data()
        fecha_desmontaje = QDate.fromString(
            str(modelo.index(fila, 13).data()), "dd/MM/yyyy")
        motivo_desmontaje = modelo.index(fila, 15).data()
        descripcion = modelo.index(fila, 16).data()

        # Cargamos los widgets
        self._view.frame.edit_id.setText(
            str(id_ent) if id_ent is not None else ""
        )
        self._view.frame.combo_proyecto.setCurrentIndex(
            self._view.frame.combo_proyecto.findText(proyecto)
        )

        if cod_color:
            self._view.frame.edit_cod_color.setText(cod_color)
            self._view.frame.button_color.setStyleSheet(
                f"background-color: {cod_color};"
            )
        else:
            self._view.frame.edit_cod_color.setText(None)
            self._view.frame.button_color.setStyleSheet(
                "background-color: transparent;"
            )

        self._view.frame.edit_nombre_acuario.setText(
            str(nombre) if nombre is not None else ""
        )
        self._view.frame.combo_urna.setCurrentIndex(
            self._view.frame.combo_urna.findText(urna)
        )
        self._view.frame.combo_tipo_acuario.setCurrentIndex(
            self._view.frame.combo_tipo_acuario.findText(tipo)
        )
        self._view.frame.edit_vol_neto.setText(
            str(volumen) if volumen is not None else ""
        )
        self._view.frame.fecha_montaje.setDate(fecha_montaje)
        self._view.frame.fecha_inicio_ciclado.setDate(fecha_inicio_ciclado)
        self._view.frame.fecha_fin_ciclado.setDate(fecha_fin_ciclado)
        self._view.frame.edit_ubicacion_acuario.setText(
            str(ubicacion) if ubicacion is not None else ""
        )
        self._view.frame.fecha_desmontaje.setDate(fecha_desmontaje)
        self._view.frame.edit_motivo_desmontaje.setText(
            str(motivo_desmontaje) if motivo_desmontaje is not None else ""
        )
        self._view.frame.text_descripcion.setPlainText(
            str(descripcion) if descripcion is not None else ""
        )

        return Result.success(id_ent)

    def _load_images(self, id_: int):
        """
        Carga las imágenes de la base de datos.
        :param id_: ID de la entidad relacionada con la fotografía
        """

        # Chequea que el registro contiene imágenes
        self.lista_fotos = (self.fdao.get_list_by_id(id_)).value

        # Mostramos las imágenes
        if len(self.lista_fotos) > 0:
            # Configurar linea de datos
            self.label_num_imagen.setText("1")
            self.label_num_total_imegenes.setText(
                str(len(self.lista_fotos))
            )
            self.show_image()

    def _choose_color(self):
        """ Selecciona un color. """

        color = QColorDialog.getColor()

        if color.isValid():
            self._view.frame.edit_cod_color.setText(color.name())
            self._view.frame.button_color.setStyleSheet(
                f"background-color: {color.name()};"
            )
        else:
            QMessageBox(
                self._view,
                self._view.windowTitle(),
                "SE LA CANCELADO LA SELECCIÓN DE COLOR"
            )

    def _open_urna_dialog(self):
        """ Abrimos el diálogo de urna. """

        # Configuramos el CONTROLADOR
        view = UrnaDialog("INSERTAR URNA")
        dao = UrnaDAO()
        mod = UrnaEntity()

        ctrl = UrnaDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_urna

        self._fill_combo_urna()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def _open_tipo_acuario_dialog(self):
        """ Abrimos el diálogo de tipo de acuario. """

        # Configuramos el CONTROLADOR
        view = TipoAcuarioDialog("INSERTAR TIPO DE ACUARIO")
        dao = TipoAcuarioDAO()
        mod = TipoAcuarioEntity()

        ctrl = TipoAcuarioDialogController(view, dao, mod)

        # Muestra el diálogo
        res = ctrl.show_modal()
        if not res.is_success:
            return

        # Configuramos el combo
        combo = self._view.frame.combo_tipo_acuario

        self._fill_combo_tipo_acuario()
        for i in range(combo.count()):
            if combo.itemData(i) == res.value.id:
                combo.setCurrentIndex(i)

    def brakdown_volumes(self, volumes: str) -> str:
        """
        Desmonta la celda del volumen y devuelve el volumen neto
        :param volumes: Cadena que representa las dimensiones del acuario
        """
        if not volumes:
            return ""

        lista = volumes.split("/")
        volumen_neto = lista[1]

        return volumen_neto
