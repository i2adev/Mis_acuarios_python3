"""
Autor:      Inigo Iturriagaetxebarria
Fecha:      04/11/2026
Comentarios:
    Control personalizado de botón de barra latteral.
"""
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QPixmap
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget

import globales


class BotonLateral(QWidget):
    """
    Botón personalizado de barra lateral.
    """

    def __init__(self, control_name: str, label: str,
                 image_rte: str | None = None, parent=None):
        super(BotonLateral, self).__init__(parent)

        # Inicializa las variables
        self.setObjectName(control_name)

        # Controles
        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)

        self.boton = QPushButton(label, parent=self)
        self.boton.setIcon(QIcon(image_rte))
        self.boton.setIconSize(QSize(32, 32))
        self.boton.setFlat(True)
        self.boton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )

        self.selected_label = QLabel()
        self.selected_label.setFixedSize(32, 32)

        pixmap = QPixmap(
            str(globales.PATH_IMAGES / "flecha-derecha-verde.png"))
        self.selected_label.setPixmap(
            pixmap.scaled(
                self.selected_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        # Monta el layoutt
        self.h_layout.addWidget(self.selected_label)
        self.h_layout.addWidget(self.boton)

    def set_active(self):
        """ Establece el control como activo."""

        self.selected_label.setVisible(True)

    def set_inactive(self):
        """ Establece el control como inactivo."""

        self.selected_label.setVisible(False)
