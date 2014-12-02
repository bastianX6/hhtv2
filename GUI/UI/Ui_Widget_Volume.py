# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_Volume.ui'
#
# Created: Thu Mar  6 19:05:07 2014
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

class Ui_WidgetVolume(object):
    def setupUi(self, WidgetVolume):
        WidgetVolume.setObjectName(_fromUtf8("WidgetVolume"))
        WidgetVolume.resize(112, 321)
        WidgetVolume.setMinimumSize(QtCore.QSize(0, 200))
        self.verticalLayout = QtGui.QVBoxLayout(WidgetVolume)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.LabelName = QtGui.QLabel(WidgetVolume)
        self.LabelName.setText(_fromUtf8(""))
        self.LabelName.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelName.setObjectName(_fromUtf8("LabelName"))
        self.verticalLayout.addWidget(self.LabelName)
        self.widget = QtGui.QWidget(WidgetVolume)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.SliderVolume = QtGui.QSlider(self.widget)
        self.SliderVolume.setMaximum(100)
        self.SliderVolume.setProperty("value", 100)
        self.SliderVolume.setOrientation(QtCore.Qt.Vertical)
        self.SliderVolume.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.SliderVolume.setTickInterval(10)
        self.SliderVolume.setObjectName(_fromUtf8("SliderVolume"))
        self.horizontalLayout_4.addWidget(self.SliderVolume)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(WidgetVolume)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout = QtGui.QGridLayout(self.widget_2)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ToolButtonMute = QtGui.QToolButton(self.widget_2)
        self.ToolButtonMute.setIconSize(QtCore.QSize(22, 22))
        self.ToolButtonMute.setCheckable(True)
        self.ToolButtonMute.setObjectName(_fromUtf8("ToolButtonMute"))
        self.gridLayout.addWidget(self.ToolButtonMute, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.LabelVolumeValue = QtGui.QLabel(self.widget_2)
        self.LabelVolumeValue.setObjectName(_fromUtf8("LabelVolumeValue"))
        self.gridLayout.addWidget(self.LabelVolumeValue, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(WidgetVolume)
        QtCore.QMetaObject.connectSlotsByName(WidgetVolume)

    def retranslateUi(self, WidgetVolume):
        WidgetVolume.setWindowTitle(_translate("WidgetVolume", "Volume", None))
        self.ToolButtonMute.setText(_translate("WidgetVolume", "Mute", None))
        self.LabelVolumeValue.setText(_translate("WidgetVolume", "100", None))

