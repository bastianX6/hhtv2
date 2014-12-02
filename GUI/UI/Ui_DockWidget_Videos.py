# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DockWidget_Videos.ui'
#
# Created: Tue Feb 18 23:09:54 2014
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

class Ui_DockWidgetVideos(object):
    def setupUi(self, DockWidgetVideos):
        DockWidgetVideos.setObjectName(_fromUtf8("DockWidgetVideos"))
        DockWidgetVideos.resize(683, 565)
        DockWidgetVideos.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.WidgetButtons = QtGui.QWidget(self.dockWidgetContents)
        self.WidgetButtons.setObjectName(_fromUtf8("WidgetButtons"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.WidgetButtons)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.WidgetButtons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.WidgetButtons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.WidgetButtons)
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 663, 491))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.MdiAreaVideos = QtGui.QMdiArea(self.scrollAreaWidgetContents)
        self.MdiAreaVideos.setMinimumSize(QtCore.QSize(640, 480))
        self.MdiAreaVideos.setMaximumSize(QtCore.QSize(640, 480))
        self.MdiAreaVideos.setObjectName(_fromUtf8("MdiAreaVideos"))
        self.horizontalLayout_2.addWidget(self.MdiAreaVideos)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        DockWidgetVideos.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidgetVideos)
        QtCore.QMetaObject.connectSlotsByName(DockWidgetVideos)

    def retranslateUi(self, DockWidgetVideos):
        DockWidgetVideos.setWindowTitle(_translate("DockWidgetVideos", "Manipular Videos", None))
        self.pushButton.setText(_translate("DockWidgetVideos", "PushButton", None))
        self.pushButton_2.setText(_translate("DockWidgetVideos", "PushButton", None))

