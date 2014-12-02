'''
Created on 13-02-2014

@author: bastian
'''

from PyQt4 import QtCore, QtGui
from GUI.UI.Ui_Widget_Volume import Ui_WidgetVolume

class WidgetVolume(QtGui.QWidget):
    '''
    classdocs
    '''


    def __init__(self,source_caps_container):
        '''
        Constructor
        '''
        
        QtGui.QWidget.__init__(self)
        self.__the_widget = Ui_WidgetVolume()
        self.__the_widget.setupUi(self)
        
        self.is_muted = False
        self.is_previewing = True
        
        self.source_caps_container = source_caps_container
        self.volume = self.__the_widget.SliderVolume.value()
        self.__the_widget.ToolButtonMute.setIcon(QtGui.QIcon.fromTheme("audio-volume-high"))
        self.connect(self.__the_widget.ToolButtonMute, QtCore.SIGNAL('clicked()'), self.__mute)
        self.connect(self.__the_widget.SliderVolume,QtCore.SIGNAL('valueChanged(int)'),self.__change_volume)
        
        
        
        
    #audio --------------------------------------------------------
    
    def __change_volume(self):
        self.volume = self.__the_widget.SliderVolume.value()
        self.__the_widget.LabelVolumeValue.setText(str(self.volume))
        
        if self.volume <=100 and self.volume >=75:
            self.__the_widget.ToolButtonMute.setIcon(QtGui.QIcon.fromTheme("audio-volume-high"))
            
        elif self.volume <75 and self.volume >=25:
            self.__the_widget.ToolButtonMute.setIcon(QtGui.QIcon.fromTheme("audio-volume-medium"))
        
        elif self.volume <25 and self.volume >0:
            self.__the_widget.ToolButtonMute.setIcon(QtGui.QIcon.fromTheme("audio-volume-low"))
            
        elif self.volume == 0:
            self.__the_widget.ToolButtonMute.setIcon(QtGui.QIcon.fromTheme("audio-volume-muted"))
        
        volume = float(self.volume / 100.0)
        self.source_caps_container.set_property("volume", "volume", volume)
        
        
           
    def __mute(self):
        if self.is_muted:
            self.is_muted = False
            self.__the_widget.SliderVolume.setEnabled(True)
            self.__change_volume()
            self.__the_widget.ToolButtonMute.setIcon(QtGui.QIcon.fromTheme("audio-volume-high"))
            
        elif not self.is_muted:
            self.is_muted = True
            self.__the_widget.SliderVolume.setEnabled(False)
            self.source_caps_container.set_property("volume", "volume", 0)
            self.__the_widget.ToolButtonMute.setIcon(QtGui.QIcon.fromTheme("audio-volume-muted"))
            
    def set_name(self,name):
        self.__the_widget.LabelName.setText(name)
        
    def set_volume(self,volume):
        self.__the_widget.SliderVolume.setValue(volume)
        self.__change_volume()
        
    def get_volume(self):
        return self.__the_widget.SliderVolume.value()
            
        