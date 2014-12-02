# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DockWidgetVolumeControl.ui'
#
# Created: Sat Feb 15 03:02:16 2014
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

class Ui_DockWidgetVolumeControl(object):
    def setupUi(self, DockWidgetVolumeControl):
        DockWidgetVolumeControl.setObjectName(_fromUtf8("DockWidgetVolumeControl"))
        DockWidgetVolumeControl.resize(695, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DockWidgetVolumeControl.sizePolicy().hasHeightForWidth())
        DockWidgetVolumeControl.setSizePolicy(sizePolicy)
        DockWidgetVolumeControl.setMinimumSize(QtCore.QSize(90, 300))
        DockWidgetVolumeControl.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 675, 261))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.LayoutVolumeControl = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.LayoutVolumeControl.setObjectName(_fromUtf8("LayoutVolumeControl"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        DockWidgetVolumeControl.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidgetVolumeControl)
        QtCore.QMetaObject.connectSlotsByName(DockWidgetVolumeControl)

    def retranslateUi(self, DockWidgetVolumeControl):
        DockWidgetVolumeControl.setWindowTitle(_translate("DockWidgetVolumeControl", "Control de Volumen", None))

