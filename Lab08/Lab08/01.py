import sys
from PySide.QtCore import*
from PySide.QtGui import*
from shape1 import Simple_drawing_window1
from shape2 import Simple_drawing_window2
from shape3 import Simple_drawing_window3

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        Simple_drawing_window1().draw(p)
        Simple_drawing_window2().draw(p)
        Simple_drawing_window3().draw(p)

        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
