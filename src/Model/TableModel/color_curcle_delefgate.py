"""
Autor:  Inigo Iturriagaetxebarria
Fecha:  21/11/2025
Comentarios:
    Delegado que dibuja un circulo de color al lado del nombre del acuario.
"""

from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QColor, QPainter, QFontMetrics
from PyQt6.QtWidgets import QStyledItemDelegate


class ColorCircleDelegate(QStyledItemDelegate):

    def paint(self, painter: QPainter, option, index):
        data = index.data()  # Espera un dict:
        # {"text": "Acuario 1", "color": "#FF0000"}

        if not isinstance(data, dict):
            super().paint(painter, option, index)
            return

        text = data.get("text", "")
        color_hex = data.get("color", "#000000")

        painter.save()

        # Fondo seleccionado
        if option.state & QStyledItemDelegate.StateFlag.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())

        # === círculo ===
        circle_diameter = 14
        margin = 6

        circle_rect = QRect(
            option.rect.left() + margin,
            option.rect.center().y() - circle_diameter // 2,
            circle_diameter,
            circle_diameter,
        )

        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QColor(color_hex))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(circle_rect)

        # === texto ===
        painter.setPen(option.palette.text().color())
        painter.setFont(option.font)

        fm = QFontMetrics(option.font)
        text_x = circle_rect.right() + margin
        text_y = option.rect.center().y() + fm.ascent() // 2 - 2

        painter.drawText(text_x, text_y, text)

        painter.restore()

    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        size.setHeight(22)
        return size

    # from PyQt6.QtCore import QRect, Qt
    # from PyQt6.QtGui import QPainter
    # from PyQt6.QtWidgets import QStyledItemDelegate
    #
    #
    # class ColorCircleDelegate(QStyledItemDelegate):
    #     def paint(self, painter: QPainter, option, index):
    #         painter.save()
    #
    #         # Texto del nombre
    #         text = index.data(Qt.ItemDataRole.DisplayRole)
    #
    #         # Color en DecorationRole
    #         color = index.data(Qt.ItemDataRole.DecorationRole)
    #
    #         rect = option.rect
    #         circle_size = 14
    #         margin = 6
    #
    #         # --- Dibujar círculo ---
    #         if color:
    #             painter.setBrush(color)
    #             painter.setPen(Qt.PenStyle.NoPen)
    #             circle_rect = QRect(
    #                 rect.x() + margin,
    #                 rect.y() + (rect.height() - circle_size) // 2,
    #                 circle_size,
    #                 circle_size
    #             )
    #             painter.drawEllipse(circle_rect)
    #
    #             # Ajustar zona para el texto
    #             text_x = rect.x() + circle_size + margin * 2
    #         else:
    #             text_x = rect.x() + margin
    #
    #         # --- Dibujar texto ---
    #         painter.setPen(option.palette.text().color())
    #         painter.setFont(option.font)
    #
    #         painter.drawText(
    #             text_x,
    #             rect.y(),
    #             rect.width() - (text_x - rect.x()),
    #             rect.height(),
    #             int(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft),
    #             text
    #         )
    #
    #         painter.restore()
