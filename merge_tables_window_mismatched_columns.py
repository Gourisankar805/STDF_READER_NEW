# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Merge_Tables_Window_mismatched_columns.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(746, 307)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(10, 30, 731, 191))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 270, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 270, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 270, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(660, 230, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(580, 230, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Insert rows - Mismatached columns"))
        self.label.setText(_translate("Form", "Mismatched columns names:"))
        self.pushButton.setText(_translate("Form", "Back"))
        self.pushButton_3.setText(_translate("Form", "Finish"))
        self.pushButton_2.setText(_translate("Form", "Next"))
        self.pushButton_5.setText(_translate("Form", "Help"))
        self.pushButton_4.setText(_translate("Form", "Cancel"))
        self.pushButton_6.setText(_translate("Form", "Clear All"))
        self.pushButton_7.setText(_translate("Form", "Select All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

