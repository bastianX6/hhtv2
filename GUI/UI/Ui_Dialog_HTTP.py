# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_HTTP.ui'
#
# Created: Thu Feb 27 19:32:02 2014
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

class Ui_DialogHTTP(object):
    def setupUi(self, DialogHTTP):
        DialogHTTP.setObjectName(_fromUtf8("DialogHTTP"))
        DialogHTTP.resize(500, 100)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogHTTP.sizePolicy().hasHeightForWidth())
        DialogHTTP.setSizePolicy(sizePolicy)
        DialogHTTP.setMinimumSize(QtCore.QSize(500, 0))
        self.verticalLayout = QtGui.QVBoxLayout(DialogHTTP)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogHTTP)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 1)
        self.LabelVideo = QtGui.QLabel(self.widget)
        self.LabelVideo.setObjectName(_fromUtf8("LabelVideo"))
        self.gridLayout.addWidget(self.LabelVideo, 0, 9, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.LineEditPortAudio = QtGui.QLineEdit(self.widget)
        self.LineEditPortAudio.setEnabled(False)
        self.LineEditPortAudio.setObjectName(_fromUtf8("LineEditPortAudio"))
        self.gridLayout.addWidget(self.LineEditPortAudio, 2, 7, 1, 1)
        self.LineEditAddressVideo = QtGui.QLineEdit(self.widget)
        self.LineEditAddressVideo.setObjectName(_fromUtf8("LineEditAddressVideo"))
        self.gridLayout.addWidget(self.LineEditAddressVideo, 0, 2, 1, 1)
        self.LineEditAddressAudio = QtGui.QLineEdit(self.widget)
        self.LineEditAddressAudio.setEnabled(False)
        self.LineEditAddressAudio.setObjectName(_fromUtf8("LineEditAddressAudio"))
        self.gridLayout.addWidget(self.LineEditAddressAudio, 2, 2, 1, 1)
        self.LineEditPortVideo = QtGui.QLineEdit(self.widget)
        self.LineEditPortVideo.setObjectName(_fromUtf8("LineEditPortVideo"))
        self.gridLayout.addWidget(self.LineEditPortVideo, 0, 7, 1, 1)
        self.LabelAudio = QtGui.QLabel(self.widget)
        self.LabelAudio.setObjectName(_fromUtf8("LabelAudio"))
        self.gridLayout.addWidget(self.LabelAudio, 2, 9, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 6, 1, 1)
        self.CheckBoxHTTPVideo = QtGui.QCheckBox(self.widget)
        self.CheckBoxHTTPVideo.setChecked(True)
        self.CheckBoxHTTPVideo.setTristate(False)
        self.CheckBoxHTTPVideo.setObjectName(_fromUtf8("CheckBoxHTTPVideo"))
        self.gridLayout.addWidget(self.CheckBoxHTTPVideo, 0, 0, 1, 1)
        self.CheckBoxHTTPAudio = QtGui.QCheckBox(self.widget)
        self.CheckBoxHTTPAudio.setObjectName(_fromUtf8("CheckBoxHTTPAudio"))
        self.gridLayout.addWidget(self.CheckBoxHTTPAudio, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.ButtonBox = QtGui.QDialogButtonBox(DialogHTTP)
        self.ButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.ButtonBox.setObjectName(_fromUtf8("ButtonBox"))
        self.verticalLayout.addWidget(self.ButtonBox)

        self.retranslateUi(DialogHTTP)
        QtCore.QObject.connect(self.ButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogHTTP.accept)
        QtCore.QObject.connect(self.ButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogHTTP.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogHTTP)

    def retranslateUi(self, DialogHTTP):
        DialogHTTP.setWindowTitle(_translate("DialogHTTP", "Abrir link HTTP", None))
        self.label_3.setText(_translate("DialogHTTP", ":", None))
        self.LabelVideo.setText(_translate("DialogHTTP", "/videofeed", None))
        self.label.setText(_translate("DialogHTTP", "http://", None))
        self.label_2.setText(_translate("DialogHTTP", "http://", None))
        self.LabelAudio.setText(_translate("DialogHTTP", "/audio.wav", None))
        self.label_4.setText(_translate("DialogHTTP", ":", None))
        self.CheckBoxHTTPVideo.setText(_translate("DialogHTTP", "Solo Video", None))
        self.CheckBoxHTTPAudio.setText(_translate("DialogHTTP", "Solo Audio", None))

