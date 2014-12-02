'''
Created on 26-12-2013

@author: bastian
'''

from PyQt4 import QtCore, QtGui
from GUI.Actions.Widget_Generic import WidgetGeneric

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

from Containers.SourceContainer import SourceContainer
from Containers.CapsContainer import CapsContainer
from Containers.MixerPreviewContainer import MixerPreviewContainer

from GUI.Actions.Widget_VideoPreview import WidgetVideoPreview
from Config.GlobalVars import Defaults

class WidgetV4L2(WidgetGeneric):
    '''
    classdocs
    '''


    def __init__(self,main_window,mdiarea,mixer,device_name,the_uri):
        '''
        Constructor
        '''
        
        super().__init__(main_window,mixer,False,True)
        
        self.have_uri = True
        self.the_uri = the_uri
        self.device_name = device_name
        self.video_width = self._the_widget.SliderWidth.value()
        self.video_height = self._the_widget.SliderHeight.value()
        self.video_alpha = self._the_widget.SliderAlpha.value()
        self.video_framerate = self._the_widget.SpinBoxFramerate.value()
        
        self.mdiarea = mdiarea
        self.set_name("Webcam")
        self.create_subwindow_video()
        self.mixer.stop_pipeline()
        self.__create_stream()
        self.mixer.play_pipeline()
        
        
        self.hide_tabs(True, False)
        
    #--------------------------------------------------------  
    
    def __create_stream(self):
        string_width = "width="+str(self.video_width)
        string_height = "height="+str(self.video_height)
        string_framerate = "framerate="+str(self.video_framerate)+"/1"
        
        self.videocaps_string = "video/x-raw,"+string_width+","+string_height+",format="+Defaults.video_format
        
        #CREATE CONTAINERS -------------------------------------------------------------------------
        self.source = SourceContainer(self.have_audio,self.have_video,self.have_uri)
        self.source_caps = CapsContainer(self.source.have_audio,self.source.have_video)
        
        self.preview_widget = MixerPreviewContainer(self.have_audio,self.have_video,self.mixer.bus,self._the_widget.WidgetPreview.winId())
        self.preview_subwindow = MixerPreviewContainer(self.have_audio,self.have_video,self.mixer.bus,self.subwindow_video.get_winId())
        self.preview_caps = CapsContainer(False,self.source.have_video)
        
        
        #ADD ELEMENTS ------------------------------------------------------------------------------
        
        self.mixer.add_container_to_pipeline(self.source)
        self.mixer.add_container_to_pipeline(self.source_caps)
        
        self.mixer.add_container_to_pipeline(self.preview_caps)
        self.mixer.add_container_to_pipeline(self.preview_widget)
        self.mixer.add_container_to_pipeline(self.preview_subwindow)
        
        #CREATE GHOST PADS -------------------------------------------------------------------------
        self.source.create_ghost_src_pad()
        self.source.create_ghost_src_pad("","video_preview1")
        self.source.create_ghost_src_pad("","video_preview2")
        
        self.source_caps.create_ghost_sink_pads()
        self.source_caps.create_ghost_src_pads()
        
        self.preview_widget.create_ghost_sink_pads()
        self.preview_subwindow.create_ghost_sink_pads()
        
        self.preview_caps.create_ghost_sink_pads()
        self.preview_caps.create_ghost_src_pads()
        
        #LINK CONTAINERS ELEMENTS-------------------------------------------------------------------
        #self.source.link_to_tee()
        self.source_caps.link_caps_elements()
        self.preview_caps.link_caps_elements()
        
        #LINK CONTAINERS ---------------------------------------------------------------------------
        
        self.source.link_containers("video_src", self.source_caps, "video_sink")
        self.source.link_containers("video_preview1", self.preview_caps, "video_sink")     
        self.preview_caps.link_containers("video_src", self.preview_widget, "video_sink")
        self.source.link_containers("video_preview2", self.preview_subwindow, "video_sink")

        
        #SET ELEMENTS PROPERTIES -------------------------------------------------------------------
        self.source_caps.set_caps("videocaps", self.videocaps_string)
        self.preview_caps.set_caps("videocaps", self.videocaps_string)
        self.source_caps.set_properties()
        self.preview_caps.set_properties()
        self.source.set_property("uridecodebin", "uri", self.the_uri)
        
        
        self.source_caps.block_pads(self.link_to_audiomixer,self.link_to_videomixer)
        
        self.source.set_state_playing()
        self.source_caps.set_state_playing()
        self.preview_widget.set_state_playing()
        self.preview_subwindow.set_state_playing()
        self.preview_caps.set_state_playing()
        
        
    def get_caps_container(self):
        return self.source_caps
    
    def create_subwindow_video(self):
        self.subwindow_video = WidgetVideoPreview(self,self.mdiarea)
        self.subwindow_video.set_name(self.name)
        
    def set_source_settings(self,source_class):
        source_class.set_source_properties("Webcam",self.the_uri,self.device_name)