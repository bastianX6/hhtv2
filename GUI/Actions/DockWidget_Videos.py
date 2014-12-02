'''
Created on 14-02-2014

@author: bastian
'''

from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_DockWidget_Videos import Ui_DockWidgetVideos

from Containers.XVideoContainer import XVideoContainer

class DockWidgetVideos(QtGui.QDockWidget):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        QtGui.QWidget.__init__(self)
        self.__the_widget = Ui_DockWidgetVideos()
        self.__the_widget.setupUi(self)
        self.__the_widget.WidgetButtons.hide()
        
        
    def add_subwindow(self,widget):

        self.__the_widget.MdiAreaVideos.addSubWindow(widget)
        widget.show()
        
        
    def remove_subwindow(self,widget):

        self.__the_widget.MdiAreaVideos.removeSubWindow(widget)
        widget.close()
        
    def get_mdiarea(self):
        return self.__the_widget.MdiAreaVideos
        