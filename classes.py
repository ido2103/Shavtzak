from funcs import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QListWidget, QListWidgetItem


class MyWindow(QMainWindow):
    def __init__(self, dict):
        super(MyWindow, self).__init__()
        self.setGeometry(500, 200, 500, 500)
        self.setWindowTitle("Shavtzak Maker")
        self.initUI(dict)
        self.makePerfect = False
        self.index = 0


    def initUI(self, dict):
        self.removed_list = {}

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()


        self.tabs.resize(500, 500)
        self.tabs.addTab(self.tab1, "Main")
        self.tabs.addTab(self.tab2, "Soldiers")

        self.tab2.layout = QVBoxLayout(self)
        self.tab2.setLayout(self.tab2.layout)

        self.tab1.layout = QVBoxLayout(self)
        self.tab1.setLayout(self.tab1.layout)

        self.layout().addWidget(self.tabs)
        self.setLayout(self.layout())

        self.label = QtWidgets.QLabel(self)
        self.label.setText("לחץ כאן כדי ליצור שבצק")
        self.label.adjustSize()
        self.label.move(5, 445)
        self.tab1.layout.addWidget(self.label)


        self.siurimEdit = QtWidgets.QLineEdit(self)
        self.siurimEdit.setText("2")
        self.siurimEdit.move(5, 25)
        self.tab1.layout.addWidget(self.siurimEdit)

        self.siurimLabel = QtWidgets.QLabel(self)
        self.siurimLabel.setText("מספר סיורים")
        self.siurimLabel.adjustSize()
        self.siurimLabel.move(39, 5)
        self.tab1.layout.addWidget(self.siurimLabel)

        self.SiurimNumEdit = QtWidgets.QLineEdit(self)
        self.SiurimNumEdit.setText("1")
        self.SiurimNumEdit.move(5, 85)
        self.tab1.layout.addWidget(self.SiurimNumEdit)

        self.SiurimNumLabel = QtWidgets.QLabel(self)
        self.SiurimNumLabel.setText("מספר אנשים בסיור")
        self.SiurimNumLabel.adjustSize()
        self.SiurimNumLabel.move(8, 65)
        self.tab1.layout.addWidget(self.SiurimNumLabel)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("צור שבצק")
        self.b1.move(5, 465)
        self.b1.clicked.connect(lambda: cycle2(dict, int(self.siurimEdit.text()), int(self.SiurimNumEdit.text()), self.makePerfect, int(self.attemptsmEdit.text()), self.index, self.removed_list))
        self.tab1.layout.addWidget(self.b1)


        self.perfectLabel = QtWidgets.QLabel(self)
        self.perfectLabel.setText("לחץ על מנת לאפשר שבצק מושלם.")
        self.perfectLabel.adjustSize()
        self.perfectLabel.move(320, 0)
        self.tab1.layout.addWidget(self.perfectLabel)

        self.perfectbutton = QtWidgets.QPushButton("לחץ", self)
        self.perfectbutton.setGeometry(380, 20, 100, 50)
        self.perfectbutton.setCheckable(True)
        self.perfectbutton.clicked.connect(self.checkPerfectButton)
        self.perfectbutton.setStyleSheet("background-color : lightgrey")
        self.tab1.layout.addWidget(self.perfectbutton)

        self.dropdownLabel = QtWidgets.QLabel(self)
        self.dropdownLabel.setText("לחץ על מנת לבחור מצב שבצק")
        self.dropdownLabel.adjustSize()
        self.dropdownLabel.move(340, 87)
        self.tab1.layout.addWidget(self.dropdownLabel)


        self.dropdown = QtWidgets.QComboBox(self)
        self.dropdown.addItems(['רגיל', "סבב מפ", "סבב סמפ"])
        self.dropdown.move(380, 110)
        self.dropdown.currentIndexChanged.connect(self.index_changed)
        self.tab1.layout.addWidget(self.dropdown)

        self.attempts = QtWidgets.QLabel(self)
        self.attempts.setText("לחץ כדי להזין כמה נסיונות לשבצק המושלם")
        self.attempts.move(276, 150)
        self.attempts.adjustSize()
        self.tab1.layout.addWidget(self.attempts)

        self.attemptsmEdit = QtWidgets.QLineEdit(self)
        self.attemptsmEdit.setText("200")
        self.attemptsmEdit.move(380, 170)
        self.tab1.layout.addWidget(self.attemptsmEdit)

        self.soldierList = QListWidget(self)
        for i in dict:
            self.soldierList.addItem(i)
        self.soldierList.clicked.connect(lambda: self.item_clicked(self.soldierList))
        self.tab2.layout.addWidget(self.soldierList)

        self.removedList = QListWidget(self)
        for i in self.removed_list:
            self.removedList.addItem(i)
        self.removedList.clicked.connect(lambda: self.item_clicked(self.removedList))
        self.tab2.layout.addWidget(self.removedList)

    def checkPerfectButton(self):
        if self.perfectbutton.isChecked():
            self.perfectbutton.setStyleSheet("background-color : lightblue")
            self.makePerfect = True
        else:
            self.perfectbutton.setStyleSheet("background-color : lightgrey")
            self.makePerfect = False

    def item_clicked(self, list):
        if list == self.soldierList:
            item = self.soldierList.currentItem()
            row = self.soldierList.currentRow()
            if item.text() not in self.removed_list:
                self.removed_list.update({item.text(): row})
                self.removedList.addItem(item.text())
                self.soldierList.takeItem(row)

        elif list == self.removedList:
            item1 = self.removedList.currentItem()
            row = self.removedList.currentRow()
            self.removed_list.pop(item1.text())
            self.removedList.takeItem(row)
            self.soldierList.addItem(item1.text())

    def index_changed(self, index):
        self.index = index
        print(index)
