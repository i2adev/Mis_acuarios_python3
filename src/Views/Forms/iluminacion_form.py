"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      23/11/2025
Comentarios:
    Módulo que contiene los controles del formulario de la entidad ILUMINACIÓN.
"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QIntValidator, QDoubleValidator
from PyQt6.QtWidgets import QFrame, QLabel, QLineEdit, QPlainTextEdit, \
    QVBoxLayout, QHBoxLayout, QApplication, QComboBox, QPushButton, QGroupBox, \
    QCheckBox

from CustomControls.nullable_date_edit import NullableDateEdit


class IluminacionForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad ILUMINACIÓN.
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
        self.layout_first_line = QHBoxLayout()
        self.layout_first_line.setContentsMargins(0, 0, 0, 20)
        ### ID
        self.layout_id = QVBoxLayout()
        ### Marca
        self.layout_marca = QVBoxLayout()
        self.layout_combo_marca = QHBoxLayout()
        ### Modelo
        self.layout_modelo = QVBoxLayout()
        ### Número de serie
        self.layout_num_serie = QVBoxLayout()

        ## Segunda línea
        self.layout_second_line = QHBoxLayout()
        self.layout_second_line.setContentsMargins(0, 0, 0, 20)
        ### Tipo de iluminación
        self.layout_tipo_iluminacion = QVBoxLayout()
        self.layout_combo_tipo_iluminacion = QHBoxLayout()
        ### Tipo de control
        self.layout_control_iluminacion = QVBoxLayout()
        self.layout_combo_control_iluminacion = QHBoxLayout()
        ### Potencia
        self.layout_potencia = QVBoxLayout()

        ## Tercera línea
        self.layout_third_line = QHBoxLayout()
        self.layout_third_line.setContentsMargins(0, 0, 0, 20)
        ### Temperatura de color
        self.layout_temperatura = QVBoxLayout()
        ### Color
        self.layout_color = QVBoxLayout()
        ### Longitud
        self.layout_longitud = QVBoxLayout()
        ### Anchura
        self.layout_anchura = QVBoxLayout()
        ### Flujo lumínico
        self.layout_flujo_luminico = QVBoxLayout()

        ## Cuarta linea
        self.layout_fourth_line = QHBoxLayout()
        self.layout_fourth_line.setContentsMargins(0, 0, 0, 20)
        ### Fecha de alta
        self.layout_fecha_alta = QVBoxLayout()
        ### Fecha de baja
        self.layout_fecha_baja = QVBoxLayout()
        ### Motivo de la baja
        self.layout_motivo_baja = QVBoxLayout()
        ### Checkboxes
        self.layout_check_boxes = QVBoxLayout()

        ## Quinta linea
        self.layout_descripcion = QVBoxLayout()

        # Controles
        ## Etiquetas
        self.label_id = QLabel("ID")
        self.label_marca = QLabel("MARCA")
        self.label_modelo = QLabel("MODELO")
        self.label_num_serie = QLabel("NÚM. SERIE")
        self.label_tipo_iluminacion = QLabel("TIPO ILUMINACIÓN")
        self.label_control_iluminacion = QLabel("TIPO CONTROL")
        self.label_potencia = QLabel("POTENCIA")
        self.label_flujo_luminico = QLabel("FLUJO LUMÍNICO")
        self.label_temperatura = QLabel("TEMPERATURA")
        self.label_flujo_luminico = QLabel("FLUJO LUMÍNICO")
        self.label_longitud = QLabel("LONGITUD")
        self.label_fecha_alta = QLabel("FECHA ALTA")
        self.label_fecha_baja = QLabel("FECHA BAJA")
        self.label_motivo_baja = QLabel("MOTIVO DE BAJA")
        self.label_anchura = QLabel("ANCHURA")
        self.label_descripcion = QLabel("DESCRICION")

        ## Check boxes
        self.check_espectro_completo = QCheckBox("ESPECTRO COMPLETO")
        self.check_espectro_completo.setChecked(False)
        self.check_intensidad_regulable = QCheckBox("INTENIDAD REGULABLE")
        self.check_intensidad_regulable.setChecked(False)

        ## Textos
        self.edit_id = QLineEdit()
        self.edit_id.setFixedWidth(50)
        self.edit_id.setEnabled(False)
        self.edit_id.setObjectName("edit_id")

        self.edit_modelo = QLineEdit()
        self.edit_modelo.setMinimumWidth(250)
        self.edit_modelo.setObjectName("edit_modelo")
        self.edit_modelo.setToolTip(
            """
            <h2>Modelo de luminaria</h2><br>
            En este campo se inserta el modelo de la luminaria. Este es un 
            campo <b>obligatorio</b>.
            """
        )

        self.edit_num_serie = QLineEdit()
        self.edit_num_serie.setMinimumWidth(250)
        self.edit_num_serie.setObjectName("edit_num_serie")
        self.edit_num_serie.setToolTip(
            """
            <h2>Número de serie</h2><br>
            En este campo se inserta el número de serie de la luminaria. Este 
            es un campo <b>obligatorio</b>.
            """
        )

        self.edit_potencia = QLineEdit()
        self.edit_potencia.setObjectName("edit_potencia")
        self.edit_potencia.setValidator(QIntValidator())
        self.edit_potencia.setToolTip(
            """
            <h2>Potencia de la luminaria</h2><br>
            En este campo se inserta la potencia de la luminaria en vatios (w).
            """
        )

        self.edit_flujo_luminico = QLineEdit()
        self.edit_flujo_luminico.setObjectName("edit_flujo_luminico")
        self.edit_flujo_luminico.setValidator(QIntValidator())
        self.edit_flujo_luminico.setToolTip(
            """
            <h2>Flujo lumínico de la luminaria</h2><br>
            En este campo se inserta el flujo lumínico que ofrece la luminaria.
            """
        )

        self.edit_temperatura = QLineEdit()
        self.edit_temperatura.setObjectName("edit_temperatura")
        self.edit_temperatura.setValidator(QIntValidator())
        self.edit_temperatura.setToolTip(
            """
            <h2>Temperatura de color</h2><br>
            En este campo se inserta la temperatura de color que ofrece la 
            luminaria en grados kelvin (K).
            """
        )

        self.edit_flujo_luminico = QLineEdit()
        self.edit_flujo_luminico.setObjectName("edit_flujo_luminico")
        self.edit_flujo_luminico.setValidator(QIntValidator())
        self.edit_flujo_luminico.setToolTip(
            """
            <h2>Color</h2><br>
            En este campo se inserta el color de la luminaria.
            """
        )

        self.edit_longitud = QLineEdit()
        self.edit_longitud.setObjectName("edit_longitud")
        self.edit_longitud.setValidator(QIntValidator())
        self.edit_longitud.setToolTip(
            """
            <h2>Longitud de la luminaria</h2><br>
            En este campo se inserta la longitud en cms de la luminaria.
            """
        )

        self.edit_anchura = QLineEdit()
        self.edit_anchura.setObjectName("edit_anchura")
        self.edit_anchura.setValidator(QIntValidator())
        self.edit_anchura.setToolTip(
            """
            <h2>Anchura de la luminaria</h2><br>
            En este campo se inserta la anchura en cms de la luminaria.
            """
        )

        self.edit_motivo_baja = QLineEdit()
        self.edit_motivo_baja.setMinimumWidth(250)
        self.edit_motivo_baja.setObjectName("edit_motivo_baja")
        self.edit_motivo_baja.setToolTip(
            """
            <h2>Motivo de la baja</h2><br>
            En este campo se inserta el el motivo por ql que se le da de 
            baja a la luminaria.
            """
        )

        self.text_descripcion = QPlainTextEdit()
        self.text_descripcion.setObjectName("text_descripcion")
        self.text_descripcion.setMinimumHeight(75)
        self.text_descripcion.setToolTip(
            """
            <h2>Descripción de la luminaria</h2>
            En este campo se inserta la descripción de la luminaria.
            """
        )

        ## Date pickers
        self.fecha_alta = NullableDateEdit()
        self.fecha_alta.setObjectName("fecha_alta")
        self.fecha_alta.setToolTip(
            """
            <h2>Fecha de alta</h2>
            En este campo se inserta la fecha de alta de la luminaria en el 
            sistema. Se puede insertar la fecha de compra.
            """
        )

        self.fecha_baja = NullableDateEdit()
        self.fecha_baja.setObjectName("fecha_baja")
        self.fecha_baja.setToolTip(
            """
            <h2>Fecha de baja</h2>
            En este campo se inserta la fecha de baja de la luminaria en el 
            sistema. Se puede insertar la fecha de compra.
            """
        )

        ## Combos
        self.combo_marca = QComboBox()
        self.combo_marca.setObjectName("combo_marca")
        self.combo_marca.setMinimumWidth(250)
        self.combo_marca.setEditable(True)
        self.combo_marca.setToolTip(
            """
            <h2>Marca de la luminaria</h2>
            En este campo se selecciona una marca. Si la marca no se 
            encuentra en la lista, puedes insertar uno pulsando en el botón 
            de la derecha. Este es un campo <b>obligatorio<b>.
            """
        )

        self.combo_tipo_iluminacion = QComboBox()
        self.combo_tipo_iluminacion.setMinimumWidth(250)
        self.combo_tipo_iluminacion.setObjectName("combo_tipo_iluminacion")
        self.combo_tipo_iluminacion.setEditable(True)
        self.combo_tipo_iluminacion.setToolTip(
            """
            <h2>Tipo de iluminación</h2>
            En este campo se selecciona el tipo de iluminación. Si el tipo 
            de iluminación no se encuentra en la lista, puedes insertar uno 
            pulsando en el botón de la derecha.
            """
        )

        self.combo_control_iluminacion = QComboBox()
        self.combo_control_iluminacion.setMinimumWidth(250)
        self.combo_control_iluminacion.setObjectName(
            "combo_control_iluminacion")
        self.combo_control_iluminacion.setEditable(True)
        self.combo_control_iluminacion.setToolTip(
            """
            <h2>Control de iluminación</h2>
            En este campo se selecciona el control con el que se gestiona 
            el funcionamiento de la luminaria. Si el tipo de iluminación 
            no se encuentra en la lista, puedes insertar uno pulsando en el 
            botón de la derecha.
            """
        )

        ## Botones
        self.button_insert_marca = QPushButton("<")
        self.button_insert_marca.setObjectName(
            "button_insert_marca")
        self.button_insert_marca.setFixedWidth(30)
        self.button_insert_marca.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_tipo_iluminacion = QPushButton("<")
        self.button_tipo_iluminacion.setObjectName(
            "button_tipo_iluminacion")
        self.button_tipo_iluminacion.setFixedWidth(30)
        self.button_tipo_iluminacion.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.button_control_iluminacion = QPushButton("<")
        self.button_control_iluminacion.setObjectName(
            "button_control_iluminacion")
        self.button_control_iluminacion.setFixedWidth(30)
        self.button_control_iluminacion.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera línea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Marca comercial
        self.layout_combo_marca.addWidget(self.combo_marca)
        self.layout_combo_marca.addWidget(self.button_insert_marca)
        self.layout_marca.addWidget(self.label_marca)
        self.layout_marca.addLayout(self.layout_combo_marca)

        ## Modelo
        self.layout_modelo.addWidget(self.label_modelo)
        self.layout_modelo.addWidget(self.edit_modelo)

        ## Número de serie
        self.layout_num_serie.addWidget(self.label_num_serie)
        self.layout_num_serie.addWidget(self.edit_num_serie)

        ## Montamos la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_marca)
        self.layout_first_line.addLayout(self.layout_modelo)
        self.layout_first_line.addLayout(self.layout_num_serie)

        # Segunda línea
        ## Tipo de iluminación
        self.layout_combo_tipo_iluminacion.addWidget(
            self.combo_tipo_iluminacion)
        self.layout_combo_tipo_iluminacion.addWidget(
            self.button_tipo_iluminacion)
        self.layout_tipo_iluminacion.addWidget(self.label_tipo_iluminacion)
        self.layout_tipo_iluminacion.addLayout(
            self.layout_combo_tipo_iluminacion)

        ## Tipo de control
        self.layout_combo_control_iluminacion.addWidget(
            self.combo_control_iluminacion)
        self.layout_combo_control_iluminacion.addWidget(
            self.button_control_iluminacion)
        self.layout_control_iluminacion.addWidget(
            self.label_control_iluminacion)
        self.layout_control_iluminacion.addLayout(
            self.layout_combo_control_iluminacion)

        ## Potencia de la luminaria
        self.layout_potencia.addWidget(self.label_potencia)
        self.layout_potencia.addWidget(self.edit_potencia)

        ## Flujo lumínico
        self.layout_flujo_luminico.addWidget(self.label_flujo_luminico)
        self.layout_flujo_luminico.addWidget(self.edit_flujo_luminico)

        ## Montamos la segunda línea
        self.layout_second_line.addLayout(self.layout_tipo_iluminacion)
        self.layout_second_line.addLayout(self.layout_control_iluminacion)
        self.layout_second_line.addLayout(self.layout_potencia)
        self.layout_second_line.addLayout(self.layout_flujo_luminico)

        # Tercera línea
        ## Temperatura
        self.layout_temperatura.addWidget(self.label_temperatura)
        self.layout_temperatura.addWidget(self.edit_temperatura)

        ## Color
        self.layout_color.addWidget(self.label_flujo_luminico)
        self.layout_color.addWidget(self.edit_flujo_luminico)

        ## Longitud
        self.layout_longitud.addWidget(self.label_longitud)
        self.layout_longitud.addWidget(self.edit_longitud)

        ## Anchura
        self.layout_anchura.addWidget(self.label_anchura)
        self.layout_anchura.addWidget(self.edit_anchura)

        ## Montaje tercera linea
        self.layout_third_line.addLayout(self.layout_temperatura)
        self.layout_third_line.addLayout(self.layout_color)
        self.layout_third_line.addLayout(self.layout_longitud)
        self.layout_third_line.addLayout(self.layout_anchura)

        # Cuarta línea
        ## Fecha de alta
        self.layout_fecha_alta.addWidget(self.label_fecha_alta)
        self.layout_fecha_alta.addWidget(self.fecha_alta)
        ## Fecha de baja
        self.layout_fecha_baja.addWidget(self.label_fecha_baja)
        self.layout_fecha_baja.addWidget(self.fecha_baja)
        ## Motivo de baja
        self.layout_motivo_baja.addWidget(self.label_motivo_baja)
        self.layout_motivo_baja.addWidget(self.edit_motivo_baja)
        ## Checkboxes
        self.layout_check_boxes.addWidget(self.check_espectro_completo)
        self.layout_check_boxes.addWidget(self.check_intensidad_regulable)

        ## Montamos la cuarta línea
        self.layout_fourth_line.addLayout(self.layout_fecha_alta)
        self.layout_fourth_line.addLayout(self.layout_fecha_baja)
        self.layout_fourth_line.addLayout(self.layout_motivo_baja)
        self.layout_fourth_line.addLayout(self.layout_check_boxes)

        # Quinta línea
        self.layout_descripcion.addWidget(self.label_descripcion)
        self.layout_descripcion.addWidget(self.text_descripcion)

        # Montaje el frame
        ## Montaje el formulario
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_second_line)
        self.layout_form.addLayout(self.layout_third_line)
        self.layout_form.addLayout(self.layout_fourth_line)
        self.layout_form.addLayout(self.layout_descripcion)
        self.setLayout(self.layout_form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = IluminacionForm()
    ventana.show()

    sys.exit(app.exec())
