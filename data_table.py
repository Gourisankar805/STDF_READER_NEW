
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Data_Table(object):
    def setupUi(self, Data_Table):
        Data_Table.setObjectName("Data_Table")
        Data_Table.resize(653, 357)
        self.tableView = QtWidgets.QTableView(Data_Table)
        self.tableView.setGeometry(QtCore.QRect(0, 10, 651, 341))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Data_Table)
        QtCore.QMetaObject.connectSlotsByName(Data_Table)

    def retranslateUi(self, Data_Table):
        _translate = QtCore.QCoreApplication.translate
        Data_Table.setWindowTitle(_translate("Data_Table", "Data_Table"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Data_Table = QtWidgets.QWidget()
    ui = Ui_Data_Table()
    ui.setupUi(Data_Table)
    Data_Table.show()
    sys.exit(app.exec_())

