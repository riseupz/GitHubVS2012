import sys
from PySide.QtCore import*
from PySide.QtGui import*

class Simple_drawing_window1():
    def draw(self, p):
        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,100), QPoint(100,110),
            QPoint(130,100), QPoint(100,150),
            ])
