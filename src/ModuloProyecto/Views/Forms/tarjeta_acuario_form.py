"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      30/10/2026
Comentarios:
    Frame de la tarjeta de acuario.
"""
import sys
from encodings import create_win32_code_page_codec
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, \
    QPushButton, QVBoxLayout

import globales
from ModuloProyecto.Models.Entities.tarjeta_acuaerio_entity import \
    TarjetaAcuarioEntity


class TarjetaAcuarioFrame(QFrame):
    """
    Frame de la tarjeta de acuario.
    """

    def __init__(self, acuario: TarjetaAcuarioEntity):
        # Llama al constructor padre
        super().__init__()

        # Establece el estilo
        self.setStyleSheet("""
            background-color: #232323;
            border: 0px solid gray;
            border-radius: 10px;
        """)

        # Inicializa las variables
        self.id = acuario.id
        self.cod_color = acuario.cod_color
        self.nombre = acuario.nombre
        self.modelo = acuario.modelo
        self.fotografia = acuario.fotografia

        # Establece las variables
        self.pixmap_selected = QPixmap(
            str(Path(globales.PATH_IMAGES) / "checked.png")
        )

        self.setObjectName("TarjetaAcuario")

        self.create_widgets()
        self.build_layout()

    def create_widgets(self):
        """ Crea los widgets de la tarjeta de acuario. """

        # Label de selección
        self.label_selected = QLabel(parent=self, text=None)
        self.label_selected.setFixedSize(25, 25)
        self.label_selected.setPixmap(self.pixmap_selected.scaled(
            self.label_selected.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
        self.label_selected.setVisible(False)

        # Label color de acuario
        self.label_color = QLabel(parent=self, text=None)
        self.label_color.setFixedSize(24, 24)
        self.label_color.setStyleSheet(f"background-color:{self.cod_color};"
                                       "border-radius: 12px;")

        # Label imagen del acuario
        self.pixmap = QPixmap()
        if self.fotografia:
            self.pixmap.loadFromData(self.fotografia)

        self.label_imagen = QLabel(parent=self, text=None)
        self.label_imagen.setFixedSize(50, 50)
        self.label_imagen.setPixmap(self.pixmap.scaled(
            self.label_imagen.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

        # Label nombre de acuario
        self.label_nombre_acuario = QLabel(parent=self, text=self.nombre)
        self.label_nombre_acuario.setStyleSheet("""
            font-family: Roboto Bold;
            font-size: 14pt;
            background-color: transparent;
        """)

        # Label modelo urna
        self.label_modelo = QLabel(parent=self, text=self.modelo)
        self.label_modelo.setStyleSheet("""
            font-family: Roboto Thin;
            font-size: 12pt;
            background-color: transparent;
        """)

        # Botón de opciones
        self.button_opciones = QPushButton("...")
        self.button_opciones.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )
        self.button_opciones.setFixedSize(50, 50)
        self.button_opciones.setStyleSheet("""
        background-color: transparent;
        """)

    def build_layout(self):
        """ Construye el layout de la tarjeta de acuario. """

        # Layout principal
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(5)

        # Layout nombre
        self.layout_nombre = QVBoxLayout(self)
        self.layout_nombre.addWidget(self.label_nombre_acuario)
        self.layout_nombre.addWidget(self.label_modelo)

        # Construimos el layout
        self.layout.addWidget(self.label_color)
        self.layout.addWidget(self.label_imagen)
        self.layout.addLayout(self.layout_nombre)
        self.layout.addWidget(self.button_opciones)
        self.layout.addWidget(self.label_selected)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = TarjetaAcuarioFrame()

    # Cargar el archivo .qss
    with open(str(Path(globales.PATH_STYLES) / "main_style.qss"), "r",
              encoding="utf-8-sig") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)

    ventana.show()
    sys.exit(app.exec())
