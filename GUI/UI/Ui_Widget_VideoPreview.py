# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_VideoPreview.ui'
#
# Created: Fri Feb 14 23:25:05 2014
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

class Ui_WidgetVideoPreview(object):
    def setupUi(self, WidgetVideoPreview):
        WidgetVideoPreview.setObjectName(_fromUtf8("WidgetVideoPreview"))
        WidgetVideoPreview.resize(400, 300)
        WidgetVideoPreview.setMinimumSize(QtCore.QSize(40, 40))
        WidgetVideoPreview.setMaximumSize(QtCore.QSize(1280, 1280))

        self.retranslateUi(WidgetVideoPreview)
        QtCore.QMetaObject.connectSlotsByName(WidgetVideoPreview)

    def retranslateUi(self, WidgetVideoPreview):
        WidgetVideoPreview.setWindowTitle(_translate("WidgetVideoPreview", "Video", None))

