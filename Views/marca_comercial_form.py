"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      28/07/2025
Commentarios:
    Módulo que contiene los controles del formulario de la entidad MARCA
    COMERCIAL.
"""

import sys

from PyQt6.QtWidgets import QFrame, QLabel, QLineEdit, QPlainTextEdit, \
    QVBoxLayout, QHBoxLayout, QApplication, QComboBox, QPushButton, QSpacerItem, \
    QSizePolicy


class MarcaComercialForm(QFrame):
    """
    Clase que contiene los controles de edición de la entidad marca comercial.
    """

    def __init__(self):
        super().__init__()

        self.setFixedHeight(275)

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Se encarga de crear los controles del formulario. """
        # Layouts
        ## Layout principal
        self.layout_form = QVBoxLayout()

        ## Layout primera linea
        self.layout_first_line = QHBoxLayout()
        ### ID
        self.layout_id = QVBoxLayout()
        ### Marca comercial
        self.layout_marca_comercial = QVBoxLayout()

        ## Segunda línea
        self.layout_second_line = QHBoxLayout()
        ### Dirección
        self.layout_direccion = QVBoxLayout()

        ### Código postal
        self.layout_cod_postal = QVBoxLayout()

        ## Tercera línea
        self.layout_third_line = QHBoxLayout()
        ### Población
        self.layout_poblacion = QVBoxLayout()

        ### Provincia
        self.layout_provincia = QVBoxLayout()

        ### País
        self.layout_pais = QVBoxLayout()
        self.layout_combo_pais = QHBoxLayout()

        ## Cuarta linea
        self.layout_fourth_line = QVBoxLayout()

        ### Observaciones
        self.layout_observaciones = QVBoxLayout()

        # Etiquetas
        self.label_id = QLabel("ID")
        self.label_id.setFixedWidth(50)
        self.label_marca = QLabel("MARCA COMERCIAL")
        self.label_direccion = QLabel("DIRECCIÓN POSTAL")
        self.label_cod_postal = QLabel("COD. POSTAL")
        self.label_poblacion = QLabel("POBLACIÓN")
        self.label_provincia = QLabel("PROVINCIA")
        self.label_pais = QLabel("PAÍS")
        self.label_observaciones = QLabel("OBSERVACIONES")

        # Textos
        self.edit_id = QLineEdit()
        self.edit_id.setEnabled(False)
        self.edit_id.setObjectName("edit_id")
        self.edit_id.setFixedWidth(50)
        self.edit_marca = QLineEdit()
        self.edit_marca.setObjectName("edit_marca")
        self.edit_direccion = QLineEdit()
        self.edit_direccion.setObjectName("edit_direccion")
        self.edit_cod_postal = QLineEdit()
        self.edit_cod_postal.setObjectName("edit_cod_postal")
        self.edit_poblacion = QLineEdit()
        self.edit_poblacion.setObjectName("edit_poblacion")
        self.edit_provincia = QLineEdit()
        self.edit_provincia.setObjectName("edit_provincia")
        self.text_observaciones = QPlainTextEdit()
        self.text_observaciones.setObjectName("text_observaciones")

        # Combos
        self.combo_pais = QComboBox()
        self.combo_pais.setObjectName("combo_pais")

        # Botones
        self.button_insert_pais = QPushButton("<")
        self.button_insert_pais.setFixedWidth(30)

    def build_layout(self):
        """ Construye el layout del frame. """

        # Primera linea
        ## ID
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.edit_id)

        ## Marca
        self.layout_marca_comercial.addWidget(self.label_marca)
        self.layout_marca_comercial.addWidget(self.edit_marca)

        ## Monta la primera linea
        self.layout_first_line.addLayout(self.layout_id)
        self.layout_first_line.addLayout(self.layout_marca_comercial)
        self.layout_first_line.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Policy.Expanding,
                        QSizePolicy.Policy.Minimum)
        )

        # Segunda línea
        ## Dirección
        self.layout_direccion.addWidget(self.label_direccion)
        self.layout_direccion.addWidget(self.edit_direccion)

        ## Código postal
        self.layout_cod_postal.addWidget(self.label_cod_postal)
        self.layout_cod_postal.addWidget(self.edit_cod_postal)

        ## Monta la segunda línea
        self.layout_second_line.addLayout(self.layout_direccion)
        self.layout_second_line.addLayout(self.layout_cod_postal)
        # self.layout_second_line.addSpacerItem(
        #     QSpacerItem(0, 0, QSizePolicy.Policy.Expanding,
        #                 QSizePolicy.Policy.Minimum)
        # )

        # Tercera línea
        ## Población
        self.layout_poblacion.addWidget(self.label_poblacion)
        self.layout_poblacion.addWidget(self.edit_poblacion)

        ## Provincia
        self.layout_provincia.addWidget(self.label_provincia)
        self.layout_provincia.addWidget(self.edit_provincia)

        ## País
        self.layout_combo_pais.addWidget(self.combo_pais)
        self.layout_combo_pais.addWidget(self.button_insert_pais)
        self.layout_pais.addWidget(self.label_pais)
        self.layout_pais.addLayout(self.layout_combo_pais)

        ## Monta la tercera línea
        self.layout_third_line.addLayout(self.layout_poblacion)
        self.layout_third_line.addLayout(self.layout_provincia)
        self.layout_third_line.addLayout(self.layout_pais)
        # self.layout_third_line.addSpacerItem(
        #     QSpacerItem(0, 0, QSizePolicy.Policy.Expanding,
        #                 QSizePolicy.Policy.Minimum)
        # )

        # Cuarta linea
        self.layout_observaciones.addWidget(self.label_observaciones)
        self.layout_observaciones.addWidget(self.text_observaciones)
        # self.layout_observaciones.addSpacerItem(
        #     QSpacerItem(0, 0, QSizePolicy.Policy.Expanding,
        #                 QSizePolicy.Policy.Minimum)
        # )

        # Montamos el frame
        self.layout_form.addLayout(self.layout_first_line)
        self.layout_form.addLayout(self.layout_second_line)
        self.layout_form.addLayout(self.layout_third_line)
        self.layout_form.addLayout(self.layout_observaciones)

        self.setLayout(self.layout_form)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MarcaComercialForm()
    ventana.setFixedWidth(800)
    ventana.setFixedHeight(600)
    ventana.show()

    sys.exit(app.exec())
