from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from funcs import append_json
import json

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout(self)
        self.setWindowTitle("Shavtzak Maker")

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(1000, 1000)

        self.tabs.addTab(self.tab1, "Main")
        self.tabs.addTab(self.tab2, "Soldiers")

        self.tab2.layout = QVBoxLayout(self)
        self.table1 = Table()
        self.tab2.layout.addWidget(self.table1)
        self.tab2.setLayout(self.tab2.layout)

        self.buttonAdd = QPushButton(self)
        self.buttonAdd.setText("Add")
        self.buttonAdd.clicked.connect(self.table1.addRow)
        self.tab2.layout.addWidget(self.buttonAdd)

        self.buttonRemove = QPushButton(self)
        self.buttonRemove.setText("Remove")
        self.buttonRemove.clicked.connect(self.table1.removeaRow)
        self.tab2.layout.addWidget(self.buttonRemove)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class Table(QTableWidget):
    def __init__(self):
        with open("soldiers.json", "r") as f:
            self.data = json.load(f)
        self.keys = ["Name:", "S.G:", "Tapuz:", "Hamal:",
                "Siur:",
                "Mitbah:",
                "Resting Hours:",
                "Mitbah Cooldown:",
                "IsHamal",
                "IsPtorMitbah",
                "IsPtorShmira",
                "IsSevevMP"]
        QTableWidget.__init__(self)
        self.setColumnCount(len(self.keys))
        self.setRowCount(len(self.data))
        self.setHorizontalHeaderLabels(self.keys)
        for r, dictionary in enumerate(self.data):
            for c, key in enumerate(dictionary):
                self.setItem(r, c, QtWidgets.QTableWidgetItem(str(dictionary[key])))
        self.itemChanged.connect(self.updateJson)

    def updateJson(self):
        list = []
        print("Updating...")
        for r, name in enumerate(self.data):
            temp_dict = {"Name:": "", "S.G:": 0, "Tapuz:": 0, "Hamal:": 0,
                         "Siur:": 0,
                         "Mitbah:": 0,
                         "Resting Hours:": 0,
                         "Mitbah Cooldown:": 0,
                         "IsHamal": 0,
                         "IsPtorMitbah": 0,
                         "IsPtorShmira": 0,
                         "IsSevevMP": 0}
            for c, info in enumerate(name):
                if self.item(r, c) is None:
                    pass
                else:
                    temp_dict.update({self.keys[c]: self.item(r, c).text()})
            list.append(temp_dict)
        with open("soldiers.json", "w") as f:
            f.seek(0)
            json.dump(list, f, indent=6)
        with open("soldiers.json", "r") as f:
            self.data = json.load(f)
        print("updated json!")

    def addRow(self): # REDO. NO NEED TO REDO THE WHOLE WINDOW JUST THE LAST ROW. ADD A ROW AND THEN FILL IT IN
        print("addRow clicked.")
        self.data = append_json("Insert Name", 0, 0, 0, 0, 0, 0, 0, False, False, False, False)
        self.insertRow(self.rowCount())
        temp_dict = {"Name:": "Insert Name", "S.G:": "0", "Tapuz:": "0", "Hamal:": "0", "Siur:": "0", "Mitbah:": "0",
                     "Resting Hours:": "0",
                     "Mitbah Cooldown:": "0",
                     "IsHamal": "False",
                     "IsPtorMitbah": "False",
                     "IsPtorShmira": "False",
                     "IsSevevMP": "False"}
        for c, key in enumerate(temp_dict):
            self.setItem(self.rowCount() - 1, c, QtWidgets.QTableWidgetItem(temp_dict[key]))
        print("Finished reprinting.")
        print("Added.")

    def removeaRow(self):
        num = QtWidgets.QInputDialog.getInt(QtWidgets.QWidget(), "RemoveRow", "Which row do you want to remove?")
        if num[1]:
            self.removeRow(num[0]-1)
        else:
            return
        d = self.data[num[0]-1]
        self.data.remove(d)
        self.updateJson()
        print("Removed row {0}".format(num[0]))
