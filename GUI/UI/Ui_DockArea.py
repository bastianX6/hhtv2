# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DockArea.ui'
#
# Created: Tue Feb 11 23:49:30 2014
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

class Ui_DockArea(object):
    def setupUi(self, DockArea):
        DockArea.setObjectName(_fromUtf8("DockArea"))
        DockArea.resize(800, 559)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DockArea.sizePolicy().hasHeightForWidth())
        DockArea.setSizePolicy(sizePolicy)
        DockArea.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(DockArea)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        DockArea.setCentralWidget(self.centralwidget)

        self.retranslateUi(DockArea)
        QtCore.QMetaObject.connectSlotsByName(DockArea)

    def retranslateUi(self, DockArea):
        DockArea.setWindowTitle(_translate("DockArea", "DockArea", None))

