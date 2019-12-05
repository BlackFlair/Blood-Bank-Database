# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InappropriateData.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InappropriateData(object):
    def setupUi(self, InappropriateData):
        InappropriateData.setObjectName("inappropriateData")
        InappropriateData.resize(285, 89)
        self.textBrowser = QtWidgets.QTextBrowser(InappropriateData)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 256, 71))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(InappropriateData)
        QtCore.QMetaObject.connectSlotsByName(InappropriateData)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ERROR</span> <span style=\" font-size:10pt; font-weight:600;\">:</span> Inappropriate data entered.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please check all the fields and try again.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InappropriateData = QtWidgets.QWidget()
    ui = Ui_InappropriateData()
    ui.setupUi(InappropriateData)
    InappropriateData.show()
    sys.exit(app.exec_())
