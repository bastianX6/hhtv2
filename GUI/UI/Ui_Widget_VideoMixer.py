# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_VideoMixer.ui'
#
# Created: Tue Dec 10 23:01:52 2013
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

class Ui_WidgetVideoMixer(object):
    def setupUi(self, WidgetVideoMixer):
        WidgetVideoMixer.setObjectName(_fromUtf8("WidgetVideoMixer"))
        WidgetVideoMixer.resize(437, 172)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetVideoMixer.sizePolicy().hasHeightForWidth())
        WidgetVideoMixer.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(WidgetVideoMixer)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(WidgetVideoMixer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.LabelHeight = QtGui.QLabel(self.groupBox)
        self.LabelHeight.setObjectName(_fromUtf8("LabelHeight"))
        self.gridLayout.addWidget(self.LabelHeight, 1, 0, 1, 1)
        self.SpinBoxHeight = QtGui.QSpinBox(self.groupBox)
        self.SpinBoxHeight.setMinimum(1)
        self.SpinBoxHeight.setMaximum(2000)
        self.SpinBoxHeight.setProperty("value", 300)
        self.SpinBoxHeight.setObjectName(_fromUtf8("SpinBoxHeight"))
        self.gridLayout.addWidget(self.SpinBoxHeight, 1, 1, 1, 2)
        self.LabelWidth = QtGui.QLabel(self.groupBox)
        self.LabelWidth.setObjectName(_fromUtf8("LabelWidth"))
        self.gridLayout.addWidget(self.LabelWidth, 0, 0, 1, 1)
        self.LabelFramerate = QtGui.QLabel(self.groupBox)
        self.LabelFramerate.setObjectName(_fromUtf8("LabelFramerate"))
        self.gridLayout.addWidget(self.LabelFramerate, 2, 0, 1, 1)
        self.ButtonPlay = QtGui.QPushButton(self.groupBox)
        self.ButtonPlay.setObjectName(_fromUtf8("ButtonPlay"))
        self.gridLayout.addWidget(self.ButtonPlay, 3, 0, 1, 3)
        self.SpinBoxFramerate = QtGui.QSpinBox(self.groupBox)
        self.SpinBoxFramerate.setMinimum(1)
        self.SpinBoxFramerate.setMaximum(30)
        self.SpinBoxFramerate.setProperty("value", 30)
        self.SpinBoxFramerate.setObjectName(_fromUtf8("SpinBoxFramerate"))
        self.gridLayout.addWidget(self.SpinBoxFramerate, 2, 1, 1, 2)
        self.SpinBoxWidth = QtGui.QSpinBox(self.groupBox)
        self.SpinBoxWidth.setMinimum(1)
        self.SpinBoxWidth.setMaximum(2000)
        self.SpinBoxWidth.setProperty("value", 400)
        self.SpinBoxWidth.setObjectName(_fromUtf8("SpinBoxWidth"))
        self.gridLayout.addWidget(self.SpinBoxWidth, 0, 1, 1, 2)
        self.ButtonStop = QtGui.QPushButton(self.groupBox)
        self.ButtonStop.setObjectName(_fromUtf8("ButtonStop"))
        self.gridLayout.addWidget(self.ButtonStop, 4, 0, 1, 3)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(WidgetVideoMixer)
        QtCore.QMetaObject.connectSlotsByName(WidgetVideoMixer)

    def retranslateUi(self, WidgetVideoMixer):
        WidgetVideoMixer.setWindowTitle(_translate("WidgetVideoMixer", "Form", None))
        self.groupBox.setTitle(_translate("WidgetVideoMixer", "Propiedades Video Mixer", None))
        self.LabelHeight.setText(_translate("WidgetVideoMixer", "Heigth", None))
        self.LabelWidth.setText(_translate("WidgetVideoMixer", "Width", None))
        self.LabelFramerate.setText(_translate("WidgetVideoMixer", "Framerate", None))
        self.ButtonPlay.setText(_translate("WidgetVideoMixer", "Play", None))
        self.ButtonStop.setText(_translate("WidgetVideoMixer", "Stop", None))

