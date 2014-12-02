'''
Created on 13-02-2014

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_DockWidget_VolumeControl import Ui_DockWidgetVolumeControl

class DockWidgetVolumeControl(QtGui.QDockWidget):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        QtGui.QWidget.__init__(self)
        self.__the_widget = Ui_DockWidgetVolumeControl()
        self.__the_widget.setupUi(self)
        
        
    def add_volume_widget(self,widget):
        self.__the_widget.LayoutVolumeControl.addWidget(widget)
        
    def remove_volume_widget(self,widget):
        self.__the_widget.LayoutVolumeControl.removeWidget(widget)
        widget.close()
        self.repaint()
        
        