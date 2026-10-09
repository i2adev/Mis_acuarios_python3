from dataclasses import dataclass

from PyQt6.QtCore import Qt, QRect, QSize
from PyQt6.QtGui import (
    QPixmap,
    QPainter,
    QStandardItemModel,
    QStandardItem,
)
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QStyledItemDelegate,
    QStyle,
    QWidget,
    QVBoxLayout,
)


# ============================================================
# ENTIDAD
# ============================================================

@dataclass
class Aquarium:
    id: int
    nombre: str
    proyecto: str
    volumen: float
    fotografia: str


# ============================================================
# DELEGATE
# ============================================================

class AquariumDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._foto_width = 100
        self._foto_height = 70

    def sizeHint(self, option, index):
        return QSize(350, 90)

    def paint(self, painter: QPainter, option, index):

        painter.save()

        # ----------------------------------------------------
        # Datos del elemento
        # ----------------------------------------------------

        aquarium = index.data(Qt.ItemDataRole.UserRole)

        if aquarium is None:
            painter.restore()
            return

        # ----------------------------------------------------
        # Fondo
        # ----------------------------------------------------

        if option.state & QStyle.StateFlag.State_Selected:
            painter.fillRect(
                option.rect,
                option.palette.highlight()
            )
        else:
            painter.fillRect(
                option.rect,
                option.palette.base()
            )

        # ----------------------------------------------------
        # Márgenes
        # ----------------------------------------------------

        margin = 8

        rect = option.rect.adjusted(
            margin,
            margin,
            -margin,
            -margin
        )

        # ----------------------------------------------------
        # Fotografía
        # ----------------------------------------------------

        foto_rect = QRect(
            rect.left(),
            rect.top(),
            self._foto_width,
            self._foto_height
        )

        pixmap = QPixmap(aquarium.fotografia)

        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                foto_rect.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            x = foto_rect.left() + (
                    foto_rect.width() - pixmap.width()
            ) // 2

            y = foto_rect.top() + (
                    foto_rect.height() - pixmap.height()
            ) // 2

            painter.drawPixmap(x, y, pixmap)

        # ----------------------------------------------------
        # Información
        # ----------------------------------------------------

        info_x = foto_rect.right() + 15

        nombre_rect = QRect(
            info_x,
            rect.top(),
            rect.width() - self._foto_width - 15,
            22
        )

        proyecto_rect = QRect(
            info_x,
            rect.top() + 23,
            rect.width() - self._foto_width - 15,
            20
        )

        volumen_rect = QRect(
            info_x,
            rect.top() + 45,
            rect.width() - self._foto_width - 15,
            20
        )

        painter.drawText(
            nombre_rect,
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter,
            aquarium.nombre
        )

        painter.drawText(
            proyecto_rect,
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter,
            f"Proyecto: {aquarium.proyecto}"
        )

        painter.drawText(
            volumen_rect,
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter,
            f"Volumen: {aquarium.volumen:.0f} L"
        )

        painter.restore()


# ============================================================
# COMBOBOX
# ============================================================

class AquariumComboBox(QComboBox):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Modelo
        self._model = QStandardItemModel(self)
        self.setModel(self._model)

        # Vista
        self.view().setSpacing(2)

        # Delegate
        self.setItemDelegate(
            AquariumDelegate(self)
        )

        # Altura del combo
        self.setMinimumHeight(40)

    def add_aquarium(self, aquarium: Aquarium):
        item = QStandardItem()

        # Texto que utilizará internamente
        item.setText(aquarium.nombre)

        # Guardamos el objeto completo
        item.setData(
            aquarium,
            Qt.ItemDataRole.UserRole
        )

        # También podemos guardar directamente el ID
        item.setData(
            aquarium.id,
            Qt.ItemDataRole.UserRole + 1
        )

        self._model.appendRow(item)

    def selected_aquarium(self):
        item = self.currentData(
            Qt.ItemDataRole.UserRole
        )

        return item


# ============================================================
# VENTANA DE PRUEBA
# ============================================================

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selección de acuario")

        layout = QVBoxLayout(self)

        self.combo_acuario = AquariumComboBox()

        layout.addWidget(self.combo_acuario)

        # ----------------------------------------------
        # Datos de ejemplo
        # ----------------------------------------------

        acuarios = [
            Aquarium(
                id=1,
                nombre="Amazonas",
                proyecto="Proyecto Amazonas",
                volumen=300,
                fotografia="amazonas.jpg"
            ),
            Aquarium(
                id=2,
                nombre="Malawi",
                proyecto="Cíclidos africanos",
                volumen=240,
                fotografia="malawi.jpg"
            ),
            Aquarium(
                id=3,
                nombre="Comunitario",
                proyecto="Proyecto principal",
                volumen=450,
                fotografia="comunitario.jpg"
            ),
        ]

        for aquarium in acuarios:
            self.combo_acuario.add_aquarium(aquarium)

        # ----------------------------------------------
        # Cambio de selección
        # ----------------------------------------------

        self.combo_acuario.currentIndexChanged.connect(
            self._on_acuario_changed
        )

    def _on_acuario_changed(self, index):

        aquarium = self.combo_acuario.selected_aquarium()

        if aquarium is None:
            return

        print("ID:", aquarium.id)
        print("Nombre:", aquarium.nombre)
        print("Proyecto:", aquarium.proyecto)
        print("Volumen:", aquarium.volumen)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    app = QApplication([])

    window = Window()
    window.resize(500, 150)
    window.show()

    app.exec()
