from funcs import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self, dict):
        super(MyWindow, self).__init__()
        self.setGeometry(500, 200, 500, 500)
        self.setWindowTitle("Shavtzak Maker")
        self.initUI(dict)

    def initUI(self, dict):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("לחץ כאן כדי ליצור שבצק")
        self.label.adjustSize()
        self.label.move(5, 445)

        self.siurimEdit = QtWidgets.QLineEdit(self)
        self.siurimEdit.setText("3")
        self.siurimEdit.move(5, 25)

        self.siurimLabel = QtWidgets.QLabel(self)
        self.siurimLabel.setText("מספר סיורים")
        self.siurimLabel.adjustSize()
        self.siurimLabel.move(39, 5)

        self.SiurimNumEdit = QtWidgets.QLineEdit(self)
        self.SiurimNumEdit.setText("1")
        self.SiurimNumEdit.move(5, 85)

        self.SiurimNumLabel = QtWidgets.QLabel(self)
        self.SiurimNumLabel.setText("מספר אנשים בסיור")
        self.SiurimNumLabel.adjustSize()
        self.SiurimNumLabel.move(8, 65)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("צור שבצק")
        self.b1.move(5, 465)
        self.b1.clicked.connect(lambda: cycle2(dict, int(self.siurimEdit.text()), int(self.SiurimNumEdit.text())))

