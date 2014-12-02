'''
Created on 11-02-2014

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_DockArea import Ui_DockArea

class DockArea(QtGui.QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        QtGui.QWidget.__init__(self)
        self.__the_widget = Ui_DockArea()
        self.__the_widget.setupUi(self)
        self.__the_widget.centralwidget.hide()
        