# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Import_Template.ui'
#
# Created: Thu Mar 13 00:28:14 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogImportTemplate(object):
    def setupUi(self, DialogImportTemplate):
        DialogImportTemplate.setObjectName(_fromUtf8("DialogImportTemplate"))
        DialogImportTemplate.resize(685, 493)
        self.verticalLayout = QtGui.QVBoxLayout(DialogImportTemplate)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(DialogImportTemplate)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtGui.QScrollArea(DialogImportTemplate)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 677, 430))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.LayoutSources = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.LayoutSources.setObjectName(_fromUtf8("LayoutSources"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.ButtonBox = QtGui.QDialogButtonBox(DialogImportTemplate)
        self.ButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.ButtonBox.setObjectName(_fromUtf8("ButtonBox"))
        self.verticalLayout.addWidget(self.ButtonBox)

        self.retranslateUi(DialogImportTemplate)
        QtCore.QObject.connect(self.ButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogImportTemplate.accept)
        QtCore.QObject.connect(self.ButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogImportTemplate.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogImportTemplate)

    def retranslateUi(self, DialogImportTemplate):
        DialogImportTemplate.setWindowTitle(_translate("DialogImportTemplate", "Asistente de Importación de Plantillas - HHTV", None))
        self.label.setText(_translate("DialogImportTemplate", "Importar Plantilla", None))

