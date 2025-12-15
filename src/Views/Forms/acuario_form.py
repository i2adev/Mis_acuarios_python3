"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      31/07/2025
Comentarios:
    Módulo que contiene los controles del formulario de la entidad ACUARIO.
"""

import sys

from CustomControls.nullable_date_edit import NullableDateEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QIntValidator
from PyQt6.QtWidgets import QApplication, QComboBox, QFrame, QGroupBox, \
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit, QPushButton, QVBoxLayout


class AcuarioForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad ACUARIO.
    """

    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """

        # Layouts
        ## Layout del formulario
        self.layout_form = QVBoxLayout()  # Layout del formulario

        ## Primera línea
        self.layout_first_line = QHBoxLayout()  # Layout de la promera linea
        self.layout_first_line.setContentsMargins(0, 0, 0, 20)
        ### ID
        self.layout_id = QVBoxLayout()
        ### ID de proyecto
        self.layout_id_proyecto = QVBoxLayout()
        ### ID de color
        self.layout_color = QVBoxLayout()
        ### Nombre
        self.layout_nombre = QVBoxLayout()
        self.layout_edit_nombre = QHBoxLayout()
        ### Urna
        self.layout_urna = QVBoxLayout()
        self.layout_combo_urna = QHBoxLayout()
        ### Tipo acuario
        self.layout_tipo_acuario = QVBoxLayout()
        self.layout_combo_tipo_acuario = QHBoxLayout()
        ### Volumen neto
        self.layout_volumen_neto = QVBoxLayout()

        ## Segunda línea
        self.layout_second_line = QHBoxLayout()
        self.layout_second_line.setContentsMargins(0, 0, 0, 20)
        self.layout_dates = QHBoxLayout()  # Layout para el group box
        ### Fecha montaje
        self.layout_fecha_montaje = QVBoxLayout()
        ### Fecha inicio ciclado
        self.layout_fecha_inicio_ciclado = QVBoxLayout()
        ### Fecha fin ciclado
        self.layout_fecha_fin_ciclado = QVBoxLayout()
        ### Fecha desmontaje
        self.layout_fecha_desmontaje = QVBoxLayout()

        ## Tercera línea
        self.layout_third_line = QHBoxLayout()
        self.layout_third_line.setContentsMargins(0, 0, 0, 20)
        ### Ubicación acuario
        self.layout_ubicacion_acuario = QVBoxLayout()
        ### Motivo desmontaje
        self.layout_motivo_desmontaje = QVBoxLayout()

        ## Cuarta línea
        self.layout_descripcion = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_proyecto = QLabel("PROYECTO")
        self.label_color = QLabel("COLOR")
        self.label_color.setFixedWidth(50)
        self.label_nombre = QLabel("NOMBRE")
        self.label_urna = QLabel("URNA")
        self.label_tipo_acuario = QLabel("TIPO ACUARIO")
        self.label_volumen_neto = QLabel("VOLUMEN NETO")
        self.label_fecha_montaje = QLabel("MONTAJE")
        self.label_fecha_inicio_ciclado = QLabel("INICIO CICLADO")
        self.label_fecha_fin_ciclado = QLabel("FIN CICLADO")
        self.label_fecha_desmontaje = QLabel("DESMONTAJE")
        self.label_ubicacion_acuario = QLabel("UBICACIÓN ACUARIO")
        self.label_motivo_desmontaje = QLabel("MOTIVO DESMONTAJE")
        self.label_descripcion = QLabel("DESCRIPCIÓN")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_id.setObjectName("edit_id")

        self.edit_cod_color = QLineEdit()
        self.edit_cod_color.setObjectName("edit_cod_color")
        self.edit_cod_color.setFixedWidth(50)
        self.edit_cod_color.setEnabled(False)

        self.edit_nombre_acuario = QLineEdit()
        self.edit_nombre_acuario.setObjectName("edit_nombre_acuario")
        self.edit_nombre_acuario.setMinimumWidth(250)
        self.edit_nombre_acuario.setToolTip(
            """
            <h2>Nombre del acuario</h2><br>
            Nombre descripctivo que se le asigna al acuario. En 
            adelante al acuario se le referira con este campo."""
        )

        self.edit_vol_neto = QLineEdit()
        self.edit_vol_neto.setObjectName("edit_vol_neto")
        self.edit_vol_neto.setValidator(QIntValidator())
        self.edit_vol_neto.setToolTip(
            """
            <h2>Volumen del neto</h2><br>
            Volumen de agua del acuario en litros una vez descontados la 
            grava del fondo y los elementos decorativos (troncos, piedras, 
            etc).
            """
        )

        self.edit_ubicacion_acuario = QLineEdit()
        self.edit_ubicacion_acuario.setObjectName("edit_ubicacion_acuario")
        self.edit_ubicacion_acuario.setToolTip(
            """<h2>Ubicación del acuario</h2><br>
            En este campo se inserta el emplazamiento del acuario. Lugar de la 
            casa en donde se instalará el acuario. 
            """
        )

        self.edit_motivo_desmontaje = QLineEdit()
        self.edit_motivo_desmontaje.setObjectName("edit_motivo_desmontaje")
        self.edit_motivo_desmontaje.setToolTip(
            """ 
            <h2>Motivo de desmontaje</h2><br>
            En este campo se inserta el motivo por el que se ha desmontado el 
            acuario.
            """
        )

        self.text_descripcion = QPlainTextEdit()
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setFixedHeight(75)
        self.text_descripcion.setToolTip(
            """ <h2>Descripción del acuario</h2><br>
            En este campo se incluirá una breve descripción del acuario.
            Se incluirán las características del mismo.
            """
        )

        # Combos
        self.combo_proyecto = QComboBox()
        self.combo_proyecto.setObjectName("combo_proyecto")
        self.combo_proyecto.setMinimumWidth(250)
        self.combo_proyecto.setToolTip(
            """
            <h2>Proyecto</h2><br>
            En este campo se seleccionará el proyecto al que pertenece el 
            acuario. Todo acuario debe pertenecer a un proyecto. Este campo es 
            obligatorio. Si en la lista no aparece el proyecto que desea, 
            puede insertarlo pulsando en el botón de la derecha.
            """
        )

        self.combo_urna = QComboBox()
        self.combo_urna.setMinimumWidth(250)
        self.combo_urna.setObjectName("combo_urna")
        self.combo_urna.setEditable(True)
        self.combo_urna.setToolTip(
            """
            <h2>Urna del acuario</h2><br>
            En este campo se selecciona la urna de la que está compuesta el 
            acuario. Este campo es obligatorio. Si en la lista no aparece la 
            urna que desea, puede insertarla pulsando en el botón de la 
            derecha.
            """
        )

        self.combo_tipo_acuario = QComboBox()
        self.combo_tipo_acuario.setMinimumWidth(250)
        self.combo_tipo_acuario.setObjectName("combo_tipo_acuario")
        self.combo_tipo_acuario.setEditable(True)
        self.combo_tipo_acuario.setToolTip(
            """
            <h2>Tipo de acuario</h2><br>
            En este campo se selecciona el tipo de acuario. Este campo es 
            obligatorio. Si no encuentra el tipo de acuario que desea, 
            puede insertarlo pulsando en el botón de la derecha.
            """
        )

        # Date pickers
        self.fecha_montaje = NullableDateEdit()
        self.fecha_montaje.setToolTip(
            """
            <h2>Fecha de montaje</h2><br>
            En este campo se inserta la fecha de montaje del acuario. La 
            fecha en la que se ha colocado la urna en el mueble. Este campo 
            es obligatorio. 
            """
        )

        self.fecha_inicio_ciclado = NullableDateEdit()
        self.fecha_inicio_ciclado.setToolTip(
            """
            <h2>Fecha de inicio del ciclado</h2><br>
            En este campo se inserta la fecha en la que se ha llenado el 
            acuario y se da inicio al proceso de ciclado del mismo.
            """
        )

        self.fecha_fin_ciclado = NullableDateEdit()
        self.fecha_fin_ciclado.setToolTip(
            """
            <h2>Fecha de finalización del ciclado</h2><br>
            En este campo se inserta la fecha de finalización del proceso de 
            ciclado del acuario.
            """
        )

        self.fecha_desmontaje = NullableDateEdit()
        # self.fecha_desmontaje.setObjectName("fecha_desmontaje")
        self.fecha_desmontaje.edit_date.setObjectName(
            "fecha_desmontaje_acuario")
        self.fecha_desmontaje.setToolTip(
            """
            <h2>Fecha de desmontaje</h2><br>
            En este campo se inserta la fecha del desmontaje del acuario.
            """
        )

        # Botones
        self.button_color = QPushButton()
        self.button_color.setFixedWidth(30)
        self.button_color.setObjectName("button_color")
        self.button_color.setStyleSheet("background-color: transparent;")
        self.button_color.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.button_insert_urna = QPushButton("<")
        self.button_insert_urna.setObjectName("button_insert_urna")
        self.button_insert_urna.setFixedWidth(30)
        self.button_insert_urna.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.button_insert_tipo_acuario = QPushButton("<")
        self.button_insert_tipo_acuario.setObjectName(
            "button_insert_tipo_acuario")
        self.button_insert_tipo_acuario.setFixedWidth(30)
        self.button_insert_tipo_acuario.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        # GroupBox
        self.dates_group_box = QGroupBox("FECHAS DEL ACUARIO")
        self.dates_group_box.setLayout(self.layout_dates)

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera línea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## ID del proyecto
        self.layout_id_proyecto.addWidget(self.label_proyecto)
        self.layout_id_proyecto.addWidget(self.combo_proyecto)

        ## ID de color
        self.layout_color.addWidget(self.label_color)
        self.layout_color.addWidget(self.edit_cod_color)

        ## Nombre
        self.layout_edit_nombre.addWidget(self.button_color)
        self.layout_edit_nombre.addWidget(self.edit_nombre_acuario)
        self.layout_nombre.addWidget(self.label_nombre)
        self.layout_nombre.addLayout(self.layout_edit_nombre)

        ## Urna
        self.layout_combo_urna.addWidget(self.combo_urna)
        self.layout_combo_urna.addWidget(self.button_insert_urna)
        self.layout_urna.addWidget(self.label_urna)
        self.layout_urna.addLayout(self.layout_combo_urna)

        ## Tipo de acuario
        self.layout_combo_tipo_acuario.addWidget(self.combo_tipo_acuario)
        self.layout_combo_tipo_acuario.addWidget(
            self.button_insert_tipo_acuario)
        self.layout_tipo_acuario.addWidget(self.label_tipo_acuario)
        self.layout_tipo_acuario.addLayout(self.layout_combo_tipo_acuario)

        ## Volumen neto
        self.layout_volumen_neto.addWidget(self.label_volumen_neto)
        self.layout_volumen_neto.addWidget(self.edit_vol_neto)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_id_proyecto)
        self.layout_first_line.addLayout(self.layout_color)
        self.layout_first_line.addLayout(self.layout_nombre)
        self.layout_first_line.addLayout(self.layout_urna)
        self.layout_first_line.addLayout(self.layout_tipo_acuario)
        self.layout_first_line.addLayout(self.layout_volumen_neto)

        # Segunda línea
        ## Fecha de montaje
        self.layout_fecha_montaje.addWidget(self.label_fecha_montaje)
        self.layout_fecha_montaje.addWidget(self.fecha_montaje)

        ## Fecha inicio ciclado
        self.layout_fecha_inicio_ciclado.addWidget(
            self.label_fecha_inicio_ciclado
        )
        self.layout_fecha_inicio_ciclado.addWidget(self.fecha_inicio_ciclado)

        ## Fecha fin ciclado
        self.layout_fecha_fin_ciclado.addWidget(self.label_fecha_fin_ciclado)
        self.layout_fecha_fin_ciclado.addWidget(self.fecha_fin_ciclado)

        ## Fecha de desmontaje
        self.layout_fecha_desmontaje.addWidget(self.label_fecha_desmontaje)
        self.layout_fecha_desmontaje.addWidget(self.fecha_desmontaje)

        ## Montamos la segunda línea
        self.layout_dates.addLayout(self.layout_fecha_montaje)
        self.layout_dates.addLayout(self.layout_fecha_inicio_ciclado)
        self.layout_dates.addLayout(self.layout_fecha_fin_ciclado)
        self.layout_dates.addLayout(self.layout_fecha_desmontaje)
        self.layout_second_line.addWidget(self.dates_group_box)

        # Tercera línea
        ## Ubicación acuario
        self.layout_ubicacion_acuario.addWidget(self.label_ubicacion_acuario)
        self.layout_ubicacion_acuario.addWidget(self.edit_ubicacion_acuario)
        ## Motivo de desmontaje
        self.layout_motivo_desmontaje.addWidget(self.label_motivo_desmontaje)
        self.layout_motivo_desmontaje.addWidget(self.edit_motivo_desmontaje)
        ## Montaje tercera linea
        self.layout_third_line.addLayout(self.layout_motivo_desmontaje)
        self.layout_third_line.addLayout(self.layout_ubicacion_acuario)

        # Cuarta línea
        self.layout_descripcion.addWidget(self.label_descripcion)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # Montamos el frame
        ## Montamos el formulario
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_second_line)
        self.layout_form.addLayout(self.layout_third_line)
        self.layout_form.addLayout(self.layout_descripcion)
        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = AcuarioForm()
    ventana.setFixedWidth(800)
    ventana.setFixedHeight(600)
    ventana.show()

    sys.exit(app.exec())
