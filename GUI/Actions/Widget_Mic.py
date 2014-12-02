'''
Created on 15-12-2013

@author: bastian
'''
from PyQt4 import QtCore, QtGui
from GUI.Actions.Widget_Generic import WidgetGeneric

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

from Containers import Utils

from Containers.SourceContainer import SourceContainer
from Containers.CapsContainer import CapsContainer
from Containers.TcpSinkContainer import TcpSinkContainer

from GUI.Actions.Widget_Volume import WidgetVolume
from GUI.Actions.Widget_VideoPreview import WidgetVideoPreview

class WidgetMic(WidgetGeneric):
    '''
    classdocs
    '''


    def __init__(self,main_window,mdiarea,mixer,device_name,device):
        '''
        Constructor
        '''
        super().__init__(main_window,mixer,True,False)
        
        self.device_name = device_name
        self.device = device
        self.have_uri = False
        
        self._the_widget.SliderWidth.setValue(100)
        self._the_widget.SliderHeight.setValue(100)
        
        self.video_width = self._the_widget.SliderWidth.value()
        self.video_height = self._the_widget.SliderHeight.value()
        self.video_alpha = self._the_widget.SliderAlpha.value()
        self.video_framerate = self._the_widget.SpinBoxFramerate.value()
        
        
        self.mdiarea = mdiarea
        self.set_name("Microfono")
        self.mixer.stop_pipeline()
        self.__create_stream()
        self.mixer.play_pipeline()
        
        self._the_widget.TabWidget.hide()
        self._the_widget.WidgetButtons.hide()
    
        
    #--------------------------------------------------------  
    
    def __create_stream(self):
        
        #CREATE CONTAINERS -------------------------------------------------------------------------
        

        self.source = SourceContainer(self.have_audio,self.have_video,self.have_uri)
        self.source_caps = CapsContainer(self.source.have_audio,self.source.have_video)  

        
        #ADD ELEMENTS ------------------------------------------------------------------------------
        
        self.source.add_element("pulsesrc", "audiosrc")
        
                
        self.mixer.add_container_to_pipeline(self.source)
        self.mixer.add_container_to_pipeline(self.source_caps)  
        
        #CREATE GHOST PADS -------------------------------------------------------------------------
        self.source.create_ghost_src_pad()
        self.source_caps.create_ghost_sink_pads()
        self.source_caps.create_ghost_src_pads()
        
        
        #LINK CONTAINERS ELEMENTS-------------------------------------------------------------------
        self.source.link_elements("audiosrc", "audiotee")
        #self.source.link_elements("audioconvert", "audiotee")
        
        
        #self.source.link_to_tee()
        self.source_caps.link_caps_elements()
        
        #LINK CONTAINERS ---------------------------------------------------------------------------
        
        #audio
        self.audiocaps_string = "audio/x-raw, format=(string)F32LE, layout=(string)interleaved, rate=(int)44000, channels=(int)2"
        self.source.link_containers("audio_src", self.source_caps, "audio_sink")
            
        #SET ELEMENTS PROPERTIES -------------------------------------------------------------------
        
        self.source_caps.set_caps("audiocaps", self.audiocaps_string)
        self.source_caps.set_property("volume", "volume", 1)
        self.source.set_property("audiosrc", "device", self.device)
        
        self.source_caps.block_pads(self.link_to_audiomixer,self.link_to_videomixer)

        self.source.set_state_playing()
        self.source_caps.set_state_playing()
        
      
 
    def play(self):
        pass
        
    
    def pause(self):
        pass
        
    def stop(self):
        pass
        
        
    def dot(self):
        pass
        
        
    def get_caps_container(self):
        return self.source_caps
    
    
    def create_widget_volume(self):
        self.widget_volume = WidgetVolume(self.get_caps_container())
        self.widget_volume.set_name(self.name)
        
    def create_subwindow_video(self):
        self.subwindow_video = WidgetVideoPreview(self,self.mdiarea)
        self.subwindow_video.set_name(self.name)
        
    def set_source_settings(self,source_class):
        source_class.set_source_properties("Pulse",self.device,self.device_name)
    