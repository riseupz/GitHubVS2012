import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Paint_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setMinimumSize(450,200)
        
    def mousePressEvent(self, e):
        print("hey")

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("A simple paint program")

        self.paint_area = Paint_area()

        layout = QVBoxLayout()
        layout.addWidget(self.paint_area)

        self.setLayout(layout)
        self.setMinimumSize(500,300)
    

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

if __name__ == "__main__":
    sys.exit(main())