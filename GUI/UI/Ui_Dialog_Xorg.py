# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Xorg.ui'
#
# Created: Wed Sep 11 13:09:57 2013
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

class Ui_DialogXorg(object):
    def setupUi(self, DialogXorg):
        DialogXorg.setObjectName(_fromUtf8("DialogXorg"))
        DialogXorg.resize(212, 86)
        self.verticalLayout = QtGui.QVBoxLayout(DialogXorg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogXorg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.LabelXorg = QtGui.QLabel(self.widget)
        self.LabelXorg.setObjectName(_fromUtf8("LabelXorg"))
        self.verticalLayout_2.addWidget(self.LabelXorg)
        self.ComboBoxXorg = QtGui.QComboBox(self.widget)
        self.ComboBoxXorg.setObjectName(_fromUtf8("ComboBoxXorg"))
        self.verticalLayout_2.addWidget(self.ComboBoxXorg)
        self.verticalLayout.addWidget(self.widget)
        self.ButtonBox = QtGui.QDialogButtonBox(DialogXorg)
        self.ButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.ButtonBox.setObjectName(_fromUtf8("ButtonBox"))
        self.verticalLayout.addWidget(self.ButtonBox)

        self.retranslateUi(DialogXorg)
        QtCore.QMetaObject.connectSlotsByName(DialogXorg)

    def retranslateUi(self, DialogXorg):
        DialogXorg.setWindowTitle(_translate("DialogXorg", "Abrir ventana X.org", None))
        self.LabelXorg.setText(_translate("DialogXorg", "Seleccionar ventana", None))

