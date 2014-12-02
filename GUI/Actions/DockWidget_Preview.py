'''
Created on 11-02-2014

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_DockWidgetPreview import Ui_DockWidgetPreview

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

from Containers.Container import Container
from Containers.CapsContainer import CapsContainer
from Containers.TcpSinkContainer import TcpSinkContainer
from Containers.XVideoContainer import XVideoContainer

from GUI.Actions.Widget_Volume import WidgetVolume

class DockWidgetPreview(QtGui.QDockWidget):
    '''
    classdocs
    '''


    def __init__(self, host_mixer,port_mixer):
        '''
        Constructor
        '''
        
        QtGui.QDockWidget.__init__(self)
        self.__the_widget = Ui_DockWidgetPreview()
        self.__the_widget.setupUi(self)

        self.host_mixer = host_mixer
        self.port_mixer = port_mixer
        self.name = "Mixer"
        
    
      
    def __init_preview(self):
        self.preview = XVideoContainer(False,True,
                                       self.host_mixer,self.port_mixer,
                                       self.__the_widget.FramePreview.winId(),False)
        
        Gst.debug_bin_to_dot_file (self.preview.pipeline,Gst.DebugGraphDetails.ALL, "dockwidget_mixer-preview")
        
        
    def play_preview(self):
        self.preview.play_pipeline()
        
    def stop_preview(self):
        self.preview.stop_pipeline()
        
    def pause_preview(self):
        self.preview.pause_pipeline()
        
        
    def get_winId(self):
        return self.__the_widget.FramePreview.winId()
        