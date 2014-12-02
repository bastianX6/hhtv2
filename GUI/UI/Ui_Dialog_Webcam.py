# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Webcam.ui'
#
# Created: Wed Sep 11 13:09:40 2013
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

class Ui_DialogWebcam(object):
    def setupUi(self, DialogWebcam):
        DialogWebcam.setObjectName(_fromUtf8("DialogWebcam"))
        DialogWebcam.resize(212, 86)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogWebcam.sizePolicy().hasHeightForWidth())
        DialogWebcam.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(DialogWebcam)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogWebcam)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.LabelSeleccionarWebcam = QtGui.QLabel(self.widget)
        self.LabelSeleccionarWebcam.setObjectName(_fromUtf8("LabelSeleccionarWebcam"))
        self.verticalLayout_2.addWidget(self.LabelSeleccionarWebcam)
        self.ComboBoxWebcam = QtGui.QComboBox(self.widget)
        self.ComboBoxWebcam.setObjectName(_fromUtf8("ComboBoxWebcam"))
        self.verticalLayout_2.addWidget(self.ComboBoxWebcam)
        self.verticalLayout.addWidget(self.widget)
        self.ButtonBox = QtGui.QDialogButtonBox(DialogWebcam)
        self.ButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.ButtonBox.setObjectName(_fromUtf8("ButtonBox"))
        self.verticalLayout.addWidget(self.ButtonBox)

        self.retranslateUi(DialogWebcam)
        QtCore.QMetaObject.connectSlotsByName(DialogWebcam)

    def retranslateUi(self, DialogWebcam):
        DialogWebcam.setWindowTitle(_translate("DialogWebcam", "Abrir Webcam", None))
        self.LabelSeleccionarWebcam.setText(_translate("DialogWebcam", "Seleccionar dispositivo", None))

