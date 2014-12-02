# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DockWidgetPreview.ui'
#
# Created: Thu Mar  6 18:51:37 2014
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

class Ui_DockWidgetPreview(object):
    def setupUi(self, DockWidgetPreview):
        DockWidgetPreview.setObjectName(_fromUtf8("DockWidgetPreview"))
        DockWidgetPreview.resize(450, 324)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DockWidgetPreview.sizePolicy().hasHeightForWidth())
        DockWidgetPreview.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("video-television"))
        DockWidgetPreview.setWindowIcon(icon)
        DockWidgetPreview.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.FramePreview = QtGui.QFrame(self.dockWidgetContents)
        self.FramePreview.setStyleSheet(_fromUtf8("background-color: rgb(128, 128, 128);"))
        self.FramePreview.setFrameShape(QtGui.QFrame.StyledPanel)
        self.FramePreview.setFrameShadow(QtGui.QFrame.Raised)
        self.FramePreview.setObjectName(_fromUtf8("FramePreview"))
        self.verticalLayout.addWidget(self.FramePreview)
        DockWidgetPreview.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidgetPreview)
        QtCore.QMetaObject.connectSlotsByName(DockWidgetPreview)

    def retranslateUi(self, DockWidgetPreview):
        DockWidgetPreview.setWindowTitle(_translate("DockWidgetPreview", "Vista Previa", None))

