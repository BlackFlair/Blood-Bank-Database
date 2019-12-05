# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 513)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewTV = QtWidgets.QTableWidget(self.centralwidget)
        self.viewTV.setGeometry(QtCore.QRect(5, 1, 441, 381))
        self.viewTV.setRowCount(20)
        self.viewTV.setColumnCount(4)
        self.viewTV.setObjectName("viewTV")
        self.BBBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BBBtn.setGeometry(QtCore.QRect(170, 400, 81, 31))
        self.BBBtn.setObjectName("BBBtn")
        self.HBtn = QtWidgets.QPushButton(self.centralwidget)
        self.HBtn.setGeometry(QtCore.QRect(170, 440, 81, 31))
        self.HBtn.setObjectName("HBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBlood_Bank = QtWidgets.QAction(MainWindow)
        self.actionBlood_Bank.setObjectName("actionBlood_Bank")
        self.actionHospital = QtWidgets.QAction(MainWindow)
        self.actionHospital.setObjectName("actionHospital")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.viewTV.setRowCount(0)


        self.BBBtn.clicked.connect(self.loadDataBB)
        self.HBtn.clicked.connect(self.loadDataH)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BBBtn.setText(_translate("MainWindow", "Blood Bank"))
        self.HBtn.setText(_translate("MainWindow", "Hospital"))
        self.actionBlood_Bank.setText(_translate("MainWindow", "Blood Bank"))
        self.actionHospital.setText(_translate("MainWindow", "Hospital"))

    def loadDataBB(self):

        connObj = sqlite3.connect('BloodBank.db')
        query = "SELECT * FROM BloodBankDetails"
        result = connObj.execute(query)
        self.viewTV.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.viewTV.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.viewTV.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))

        connObj.close()

    def loadDataH(self):
        connObj = sqlite3.connect('BloodBank.db')
        query = "SELECT * FROM HospitalDetails"
        result = connObj.execute(query)
        self.viewTV.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.viewTV.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.viewTV.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))

        connObj.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
