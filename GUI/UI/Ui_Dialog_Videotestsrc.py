# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Videotestsrc.ui'
#
# Created: Mon Nov 25 21:52:08 2013
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

class Ui_DialogVideotestsrc(object):
    def setupUi(self, DialogVideotestsrc):
        DialogVideotestsrc.setObjectName(_fromUtf8("DialogVideotestsrc"))
        DialogVideotestsrc.resize(403, 172)
        self.verticalLayout = QtGui.QVBoxLayout(DialogVideotestsrc)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogVideotestsrc)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.SpinBoxHeight = QtGui.QSpinBox(self.widget)
        self.SpinBoxHeight.setMinimum(1)
        self.SpinBoxHeight.setMaximum(2000)
        self.SpinBoxHeight.setProperty("value", 300)
        self.SpinBoxHeight.setObjectName(_fromUtf8("SpinBoxHeight"))
        self.gridLayout.addWidget(self.SpinBoxHeight, 1, 1, 1, 1)
        self.SpinBoxAlpha = QtGui.QSpinBox(self.widget)
        self.SpinBoxAlpha.setMaximum(100)
        self.SpinBoxAlpha.setProperty("value", 100)
        self.SpinBoxAlpha.setObjectName(_fromUtf8("SpinBoxAlpha"))
        self.gridLayout.addWidget(self.SpinBoxAlpha, 2, 1, 1, 1)
        self.SpinBoxWidth = QtGui.QSpinBox(self.widget)
        self.SpinBoxWidth.setMinimum(1)
        self.SpinBoxWidth.setMaximum(2000)
        self.SpinBoxWidth.setProperty("value", 400)
        self.SpinBoxWidth.setObjectName(_fromUtf8("SpinBoxWidth"))
        self.gridLayout.addWidget(self.SpinBoxWidth, 0, 1, 1, 1)
        self.LabelWidth = QtGui.QLabel(self.widget)
        self.LabelWidth.setObjectName(_fromUtf8("LabelWidth"))
        self.gridLayout.addWidget(self.LabelWidth, 0, 0, 1, 1)
        self.ComboBoxPattern = QtGui.QComboBox(self.widget)
        self.ComboBoxPattern.setObjectName(_fromUtf8("ComboBoxPattern"))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.ComboBoxPattern.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.ComboBoxPattern, 4, 1, 1, 1)
        self.LabelPattern = QtGui.QLabel(self.widget)
        self.LabelPattern.setObjectName(_fromUtf8("LabelPattern"))
        self.gridLayout.addWidget(self.LabelPattern, 4, 0, 1, 1)
        self.LabelAlpha = QtGui.QLabel(self.widget)
        self.LabelAlpha.setObjectName(_fromUtf8("LabelAlpha"))
        self.gridLayout.addWidget(self.LabelAlpha, 2, 0, 1, 1)
        self.LabelHeight = QtGui.QLabel(self.widget)
        self.LabelHeight.setObjectName(_fromUtf8("LabelHeight"))
        self.gridLayout.addWidget(self.LabelHeight, 1, 0, 1, 1)
        self.LabelFramerate = QtGui.QLabel(self.widget)
        self.LabelFramerate.setObjectName(_fromUtf8("LabelFramerate"))
        self.gridLayout.addWidget(self.LabelFramerate, 3, 0, 1, 1)
        self.SpinBoxFramerate = QtGui.QSpinBox(self.widget)
        self.SpinBoxFramerate.setMinimum(1)
        self.SpinBoxFramerate.setMaximum(30)
        self.SpinBoxFramerate.setProperty("value", 30)
        self.SpinBoxFramerate.setObjectName(_fromUtf8("SpinBoxFramerate"))
        self.gridLayout.addWidget(self.SpinBoxFramerate, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.ButtonBox = QtGui.QDialogButtonBox(DialogVideotestsrc)
        self.ButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.ButtonBox.setObjectName(_fromUtf8("ButtonBox"))
        self.verticalLayout.addWidget(self.ButtonBox)

        self.retranslateUi(DialogVideotestsrc)
        QtCore.QMetaObject.connectSlotsByName(DialogVideotestsrc)

    def retranslateUi(self, DialogVideotestsrc):
        DialogVideotestsrc.setWindowTitle(_translate("DialogVideotestsrc", "Agregar video de prueba", None))
        self.LabelWidth.setText(_translate("DialogVideotestsrc", "Width", None))
        self.ComboBoxPattern.setItemText(0, _translate("DialogVideotestsrc", "(0): smpte - SMPTE 100% color bars", None))
        self.ComboBoxPattern.setItemText(1, _translate("DialogVideotestsrc", "(1): Random (television snow)", None))
        self.ComboBoxPattern.setItemText(2, _translate("DialogVideotestsrc", "(2): black", None))
        self.ComboBoxPattern.setItemText(3, _translate("DialogVideotestsrc", "(3): white", None))
        self.ComboBoxPattern.setItemText(4, _translate("DialogVideotestsrc", "(4): red", None))
        self.ComboBoxPattern.setItemText(5, _translate("DialogVideotestsrc", "(5): green", None))
        self.ComboBoxPattern.setItemText(6, _translate("DialogVideotestsrc", "(6): blue", None))
        self.ComboBoxPattern.setItemText(7, _translate("DialogVideotestsrc", "(7): Checkers 1px", None))
        self.ComboBoxPattern.setItemText(8, _translate("DialogVideotestsrc", "(8): Checkers 2px", None))
        self.ComboBoxPattern.setItemText(9, _translate("DialogVideotestsrc", "(9): Checkers 4px", None))
        self.ComboBoxPattern.setItemText(10, _translate("DialogVideotestsrc", "(10): Checkers 8px", None))
        self.ComboBoxPattern.setItemText(11, _translate("DialogVideotestsrc", "(11): circular", None))
        self.ComboBoxPattern.setItemText(12, _translate("DialogVideotestsrc", "(12): blink", None))
        self.ComboBoxPattern.setItemText(13, _translate("DialogVideotestsrc", "(13): smpte75 - SMPTE 75% color bars", None))
        self.ComboBoxPattern.setItemText(14, _translate("DialogVideotestsrc", "(14): Zone plate", None))
        self.ComboBoxPattern.setItemText(15, _translate("DialogVideotestsrc", "(15): Gamut checkers", None))
        self.ComboBoxPattern.setItemText(16, _translate("DialogVideotestsrc", "(16): Chroma zone plate", None))
        self.ComboBoxPattern.setItemText(17, _translate("DialogVideotestsrc", "(17): Solid color", None))
        self.ComboBoxPattern.setItemText(18, _translate("DialogVideotestsrc", "(18): Moving ball", None))
        self.ComboBoxPattern.setItemText(19, _translate("DialogVideotestsrc", "(19): smpte100 - SMPTE 100% color bars", None))
        self.ComboBoxPattern.setItemText(20, _translate("DialogVideotestsrc", "(20): Bar", None))
        self.ComboBoxPattern.setItemText(21, _translate("DialogVideotestsrc", "(21): Pinwheel", None))
        self.ComboBoxPattern.setItemText(22, _translate("DialogVideotestsrc", "(22): Spokes", None))
        self.LabelPattern.setText(_translate("DialogVideotestsrc", "Pattern", None))
        self.LabelAlpha.setText(_translate("DialogVideotestsrc", "Alpha", None))
        self.LabelHeight.setText(_translate("DialogVideotestsrc", "Heigth", None))
        self.LabelFramerate.setText(_translate("DialogVideotestsrc", "Framerate", None))

