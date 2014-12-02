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
from Containers.TcpSinkContainer import TcpSinkContainer
from Containers.MixerPreviewContainer import MixerPreviewContainer

from GUI.Actions.Widget_Volume import WidgetVolume
from GUI.Actions.Widget_VideoPreview import WidgetVideoPreview

class WidgetHTTP(WidgetGeneric):
    '''
    classdocs
    '''


    def __init__(self,main_window,mdiarea,mixer,have_audio,have_video,the_uri):
        '''
        Constructor
        '''
        
        super().__init__(main_window,mixer,have_audio,have_video)
        
        self.the_uri = the_uri
        self.video_width = self._the_widget.SliderWidth.value()
        self.video_height = self._the_widget.SliderHeight.value()
        self.video_alpha = self._the_widget.SliderAlpha.value()
        self.video_framerate = self._the_widget.SpinBoxFramerate.value()
        
        self.mdiarea = mdiarea
        self.set_name("HTTP Stream")
        self.create_subwindow_video()
        
        if self.have_video:
            self.mixer.stop_pipeline()
            
        else:
            self.mixer.pipeline_ready()
            
        self.__create_stream()
        self.mixer.play_pipeline()
        
        
        
        
        self.hide_tabs(True, not self.have_video,not self.have_video)
        
    #--------------------------------------------------------  
    
    def __create_stream(self):
        string_width = "width="+str(self.video_width)
        string_height = "height="+str(self.video_height)
        string_framerate = "framerate="+str(self.video_framerate)+"/1"
        
        self.videocaps_string = "video/x-raw,"+string_width+","+string_height+","+string_framerate
        
        container_list = []
        have_uri = True
        
        if self.have_video:
            have_uri = False

        
        #CREATE CONTAINERS -------------------------------------------------------------------------
        self.source = SourceContainer(self.have_audio,self.have_video,have_uri)
        self.source_caps = CapsContainer(self.source.have_audio,self.source.have_video)
        
        container_list.append(self.source)
        container_list.append(self.source_caps)
        
        if self.have_video:
            self.preview_caps = CapsContainer(False,self.source.have_video)
            self.preview_widget = MixerPreviewContainer(self.have_audio,self.have_video,self.mixer.bus,self._the_widget.WidgetPreview.winId())
            self.preview_subwindow = MixerPreviewContainer(self.have_audio,self.have_video,self.mixer.bus,self.subwindow_video.get_winId())
            
            container_list.append(self.preview_caps)
            container_list.append(self.preview_subwindow)
            container_list.append(self.preview_widget)
        
        
        #ADD ELEMENTS ------------------------------------------------------------------------------
        
        if self.have_video:
            
            self.source.add_element("souphttpsrc", "videosrc")
            self.source.add_element("jpegparse", "jpegparse")
            self.source.add_element("jpegdec","jpegdec")
            
            self.mixer.add_container_to_pipeline(self.preview_widget)
            self.mixer.add_container_to_pipeline(self.preview_subwindow)
            self.mixer.add_container_to_pipeline(self.preview_caps)
            
            self.source.create_ghost_src_pad("","video_preview1")
            self.source.create_ghost_src_pad("","video_preview2")
            
            self.preview_widget.create_ghost_sink_pads()
            self.preview_subwindow.create_ghost_sink_pads()
            
            self.preview_caps.create_ghost_sink_pads()
            self.preview_caps.create_ghost_src_pads()
        
        
        self.mixer.add_container_to_pipeline(self.source)
        self.mixer.add_container_to_pipeline(self.source_caps)
        
        self.source.create_ghost_src_pad()
        self.source_caps.create_ghost_sink_pads()
        self.source_caps.create_ghost_src_pads()
        
        
        
        #LINK CONTAINERS ELEMENTS-------------------------------------------------------------------
        
        if self.have_video:
            self.source.link_elements("videosrc", "jpegparse")
            self.source.link_elements("jpegparse","jpegdec")
            self.source.link_elements("jpegdec", "videoconvert")
            self.source.link_elements("videoconvert","videotee")
            self.preview_caps.link_caps_elements()
        
        
        self.source_caps.link_caps_elements()
        
        #LINK CONTAINERS ---------------------------------------------------------------------------
        
        if self.have_video:
        
            self.source.link_containers("video_src", self.source_caps, "video_sink")
            self.source.link_containers("video_preview1", self.preview_caps, "video_sink")     
            self.preview_caps.link_containers("video_src", self.preview_widget, "video_sink")
            
            self.source.link_containers("video_preview2", self.preview_subwindow, "video_sink")
            
            self.source_caps.set_caps("videocaps", self.videocaps_string)
            self.preview_caps.set_caps("videocaps", self.videocaps_string)
            
            self.source_caps.set_properties()
            self.preview_caps.set_properties()
            self.source.set_property("videosrc", "location", self.the_uri)
            self.source.set_property("videosrc", "do-timestamp", True)
            self.source.set_property("videosrc", "is-live", True)
            
            self.preview_widget.set_state_playing()
            self.preview_subwindow.set_state_playing()
            self.preview_caps.set_state_playing()
            
            
        if self.have_audio:
            self.audiocaps_string = "audio/x-raw, format=(string)F32LE, layout=(string)interleaved, rate=(int)44000, channels=(int)2"
            self.source.link_containers("audio_src", self.source_caps, "audio_sink")
            self.source_caps.set_caps("audiocaps", self.audiocaps_string)
            self.source_caps.set_property("volume", "volume", 1)
            
            self.source.set_property("uridecodebin", "uri", self.the_uri)
        
        #SET ELEMENTS PROPERTIES -------------------------------------------------------------------
        
        self.source_caps.block_pads(self.link_to_audiomixer,self.link_to_videomixer)
        #self.mixer.connect_on_error(self.on_eos,container_list)
        
        
        self.source.set_state_playing()
        self.source_caps.set_state_playing()
              
        

    def get_caps_container(self):
        return self.source_caps
    
    def create_widget_volume(self):
        self.widget_volume = WidgetVolume(self.get_caps_container())
        self.widget_volume.set_name(self.name)
        
    def create_subwindow_video(self):
        self.subwindow_video = WidgetVideoPreview(self,self.mdiarea)
        self.subwindow_video.set_name(self.name)
        
        
    def on_eos(self, bus, msg,container_list):
        print("on_eos()")
        
        self.mixer.stop_pipeline()
        self.mixer.unlink_from_videomixer(self.source_caps)
            
        for cont in container_list:
            self.mixer.remove_container_from_pipeline(cont)
            

            
        self.mixer.play_pipeline()
        
        
    def set_source_settings(self,source_class):
        source_class.set_source_properties("Http",self.the_uri,None)

        