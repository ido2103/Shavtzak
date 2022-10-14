from PyQt5.QtWidgets import *
from PyQt5 import uic

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("ShavtzakGUI.ui", self)
        self.show()
        QPushButton(self)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    app.exec_()