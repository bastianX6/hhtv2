# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Microfono.ui'
#
# Created: Wed Sep 11 13:08:56 2013
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

class Ui_DialogMicrofono(object):
    def setupUi(self, DialogMicrofono):
        DialogMicrofono.setObjectName(_fromUtf8("DialogMicrofono"))
        DialogMicrofono.resize(212, 86)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogMicrofono.sizePolicy().hasHeightForWidth())
        DialogMicrofono.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(DialogMicrofono)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogMicrofono)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.LabelSeleccionarMicrofono = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelSeleccionarMicrofono.sizePolicy().hasHeightForWidth())
        self.LabelSeleccionarMicrofono.setSizePolicy(sizePolicy)
        self.LabelSeleccionarMicrofono.setObjectName(_fromUtf8("LabelSeleccionarMicrofono"))
        self.verticalLayout_2.addWidget(self.LabelSeleccionarMicrofono)
        self.ComboBoxMicrofono = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboBoxMicrofono.sizePolicy().hasHeightForWidth())
        self.ComboBoxMicrofono.setSizePolicy(sizePolicy)
        self.ComboBoxMicrofono.setObjectName(_fromUtf8("ComboBoxMicrofono"))
        self.verticalLayout_2.addWidget(self.ComboBoxMicrofono)
        self.verticalLayout.addWidget(self.widget)
        self.ButtonBox = QtGui.QDialogButtonBox(DialogMicrofono)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonBox.sizePolicy().hasHeightForWidth())
        self.ButtonBox.setSizePolicy(sizePolicy)
        self.ButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.ButtonBox.setObjectName(_fromUtf8("ButtonBox"))
        self.verticalLayout.addWidget(self.ButtonBox)

        self.retranslateUi(DialogMicrofono)
        QtCore.QMetaObject.connectSlotsByName(DialogMicrofono)

    def retranslateUi(self, DialogMicrofono):
        DialogMicrofono.setWindowTitle(_translate("DialogMicrofono", "Abrir Micrófono", None))
        self.LabelSeleccionarMicrofono.setText(_translate("DialogMicrofono", "Seleccionar dispositivo", None))

