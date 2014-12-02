# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_Source_Template.ui'
#
# Created: Thu Mar 13 19:21:22 2014
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

class Ui_WidgetSourceTemplate(object):
    def setupUi(self, WidgetSourceTemplate):
        WidgetSourceTemplate.setObjectName(_fromUtf8("WidgetSourceTemplate"))
        WidgetSourceTemplate.resize(450, 130)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetSourceTemplate.sizePolicy().hasHeightForWidth())
        WidgetSourceTemplate.setSizePolicy(sizePolicy)
        WidgetSourceTemplate.setMinimumSize(QtCore.QSize(450, 130))
        self.gridLayout = QtGui.QGridLayout(WidgetSourceTemplate)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.LabelSourceType = QtGui.QLabel(WidgetSourceTemplate)
        self.LabelSourceType.setText(_fromUtf8(""))
        self.LabelSourceType.setObjectName(_fromUtf8("LabelSourceType"))
        self.gridLayout.addWidget(self.LabelSourceType, 0, 1, 1, 2)
        self.label = QtGui.QLabel(WidgetSourceTemplate)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMargin(2)
        self.label.setIndent(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.LabelSource = QtGui.QLabel(WidgetSourceTemplate)
        self.LabelSource.setText(_fromUtf8(""))
        self.LabelSource.setObjectName(_fromUtf8("LabelSource"))
        self.gridLayout.addWidget(self.LabelSource, 1, 1, 1, 1)
        self.CheckBoxIgnoreSource = QtGui.QCheckBox(WidgetSourceTemplate)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("edit-delete"))
        self.CheckBoxIgnoreSource.setIcon(icon)
        self.CheckBoxIgnoreSource.setIconSize(QtCore.QSize(22, 22))
        self.CheckBoxIgnoreSource.setObjectName(_fromUtf8("CheckBoxIgnoreSource"))
        self.gridLayout.addWidget(self.CheckBoxIgnoreSource, 3, 0, 1, 3)
        self.label_5 = QtGui.QLabel(WidgetSourceTemplate)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setMargin(2)
        self.label_5.setIndent(0)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.LabelState = QtGui.QLabel(WidgetSourceTemplate)
        self.LabelState.setText(_fromUtf8(""))
        self.LabelState.setObjectName(_fromUtf8("LabelState"))
        self.gridLayout.addWidget(self.LabelState, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(WidgetSourceTemplate)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setMargin(2)
        self.label_3.setIndent(0)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.ToolButtonSelectSource = QtGui.QToolButton(WidgetSourceTemplate)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-open"))
        self.ToolButtonSelectSource.setIcon(icon)
        self.ToolButtonSelectSource.setIconSize(QtCore.QSize(22, 22))
        self.ToolButtonSelectSource.setObjectName(_fromUtf8("ToolButtonSelectSource"))
        self.gridLayout.addWidget(self.ToolButtonSelectSource, 1, 2, 1, 1)
        self.line = QtGui.QFrame(WidgetSourceTemplate)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 4, 0, 1, 3)
        self.ToolButtonState = QtGui.QToolButton(WidgetSourceTemplate)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("dialog-warning"))
        self.ToolButtonState.setIcon(icon)
        self.ToolButtonState.setIconSize(QtCore.QSize(22, 22))
        self.ToolButtonState.setCheckable(False)
        self.ToolButtonState.setObjectName(_fromUtf8("ToolButtonState"))
        self.gridLayout.addWidget(self.ToolButtonState, 2, 2, 1, 1)

        self.retranslateUi(WidgetSourceTemplate)
        QtCore.QMetaObject.connectSlotsByName(WidgetSourceTemplate)

    def retranslateUi(self, WidgetSourceTemplate):
        WidgetSourceTemplate.setWindowTitle(_translate("WidgetSourceTemplate", "Fuente", None))
        self.label.setText(_translate("WidgetSourceTemplate", "Tipo Fuente", None))
        self.CheckBoxIgnoreSource.setText(_translate("WidgetSourceTemplate", "No considerar esta fuente", None))
        self.label_5.setText(_translate("WidgetSourceTemplate", "Estado", None))
        self.label_3.setText(_translate("WidgetSourceTemplate", "Dispositivo", None))
        self.ToolButtonSelectSource.setText(_translate("WidgetSourceTemplate", "Seleccionar", None))
        self.ToolButtonState.setText(_translate("WidgetSourceTemplate", "...", None))

