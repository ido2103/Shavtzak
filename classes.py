from funcs import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import time


class MyWindow(QMainWindow):
    def __init__(self, dict):
        super(MyWindow, self).__init__()
        self.setGeometry(500, 200, 500, 500)
        self.setWindowTitle("Shavtzak Maker")
        self.initUI(dict)
        self.makePerfect = False
        self.index = 0

    def initUI(self, dict):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("לחץ כאן כדי ליצור שבצק")
        self.label.adjustSize()
        self.label.move(5, 445)

        self.siurimEdit = QtWidgets.QLineEdit(self)
        self.siurimEdit.setText("2")
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
        time1 = time.process_time()
        self.b1.clicked.connect(lambda: cycle2(dict, int(self.siurimEdit.text()), int(self.SiurimNumEdit.text()), self.makePerfect, int(self.attemptsmEdit.text()), self.index))
        self.b1.clicked.connect(lambda: self.updateCounter(time.process_time()-time1))


        self.counterText = QtWidgets.QLabel(self)
        self.counterText.setText("זמן: ")
        self.counterText.adjustSize()
        self.counterText.move(80, 120)

        self.counter = QtWidgets.QLabel(self)
        self.counter.move(52, 120)

        self.perfectLabel = QtWidgets.QLabel(self)
        self.perfectLabel.setText("לחץ על מנת לאפשר שבצק מושלם.")
        self.perfectLabel.adjustSize()
        self.perfectLabel.move(320, 0)

        self.perfectbutton = QtWidgets.QPushButton("לחץ", self)
        self.perfectbutton.setGeometry(380, 20, 100, 50)
        self.perfectbutton.setCheckable(True)
        self.perfectbutton.clicked.connect(self.checkPerfectButton)
        self.perfectbutton.setStyleSheet("background-color : lightgrey")

        self.dropdownLabel = QtWidgets.QLabel(self)
        self.dropdownLabel.setText("לחץ על מנת לבחור מצב שבצק")
        self.dropdownLabel.adjustSize()
        self.dropdownLabel.move(340, 87)

        self.dropdown = QtWidgets.QComboBox(self)
        self.dropdown.addItems(['רגיל', "סבב מפ", "סבב סמפ"])
        self.dropdown.move(380, 110)
        self.dropdown.currentIndexChanged.connect(self.index_changed)

        self.attempts = QtWidgets.QLabel(self)
        self.attempts.setText("לחץ כדי להזין כמה נסיונות לשבצק המושלם")
        self.attempts.move(276, 150)
        self.attempts.adjustSize()

        self.attemptsmEdit = QtWidgets.QLineEdit(self)
        self.attemptsmEdit.setText("200")
        self.attemptsmEdit.move(380, 170)

    def updateCounter(self, x):
        x = str(x)
        self.counter.setText(x[0:5])
        self.counter.adjustSize()

    def checkPerfectButton(self):
        if self.perfectbutton.isChecked():
            self.perfectbutton.setStyleSheet("background-color : lightblue")
            self.makePerfect = True
        else:
            self.perfectbutton.setStyleSheet("background-color : lightgrey")
            self.makePerfect = False
    def index_changed(self, index):
        self.index = index
        print(index)
