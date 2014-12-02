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

from Containers.FileSrcContainer import FileSrcContainer
from Containers.SourceContainer import SourceContainer
from Containers.CapsContainer import CapsContainer
from Containers.MixerPreviewContainer import MixerPreviewContainer

from GUI.Actions.Widget_Volume import WidgetVolume
from GUI.Actions.Widget_VideoPreview import WidgetVideoPreview

from Config.GlobalVars import Defaults

class WidgetFile(WidgetGeneric):
    '''
    classdocs
    '''


    def __init__(self,main_window,mdiarea,mixer,the_uri):
        '''
        Constructor
        '''
        self.the_uri =  "file://"+the_uri
        the_tuple = Utils.uri_discoverer(self.the_uri)
        super().__init__(main_window,mixer,the_tuple[0],the_tuple[1])
        
        self.is_image = the_tuple[2]
        self.mdiarea = mdiarea
        
        name = ""
        
        if self.have_audio and self.have_video:
            name= "Archivo de Audio y Video"
            
        elif self.have_audio:
            name= "Archivo de Audio"
            
        elif self.have_video and not self.is_image:
            name= "Archivo de Video"
            
        elif self.is_image:
            name = "Imagen"
            
        
        self.set_name(name)
        self.create_subwindow_video()
        self.mixer.stop_pipeline()
        self.__create_stream()
        self.mixer.play_pipeline()
        
        self.current_pos = 0
        
        
        self.hide_tabs(not self.have_audio, not self.have_video)

        self.connect(self._the_widget.ButtonPlay ,QtCore.SIGNAL('clicked()'),self.play)
        self.connect(self._the_widget.ButtonStop ,QtCore.SIGNAL('clicked()'),self.stop)
        self.connect(self._the_widget.ButtonDot ,QtCore.SIGNAL('clicked()'),self.dot)
  
        
    #--------------------------------------------------------  
    
    def __create_stream(self):
        
        #CREATE CONTAINERS -------------------------------------------------------------------------
        
        self.source = SourceContainer(self.have_audio,self.have_video)
        self.source_caps = CapsContainer(self.source.have_audio,self.source.have_video,self.is_image) 
        
        self.mixer.add_container_to_pipeline(self.source)
        self.mixer.add_container_to_pipeline(self.source_caps)  
        
        if self.have_video:
            self.preview_widget = MixerPreviewContainer(False,self.have_video,self.mixer.bus,self._the_widget.WidgetPreview.winId())
            self.preview_subwindow = MixerPreviewContainer(False,self.have_video,self.mixer.bus,self.subwindow_video.get_winId())
            self.preview_caps = CapsContainer(False,self.source.have_video,self.is_image)
            
            self.mixer.add_container_to_pipeline(self.preview_widget)
            self.mixer.add_container_to_pipeline(self.preview_subwindow)
            self.mixer.add_container_to_pipeline(self.preview_caps)
        
        
        #CREATE GHOST PADS -------------------------------------------------------------------------
        
        self.source.create_ghost_src_pad()
        self.source_caps.create_ghost_sink_pads()
        self.source_caps.create_ghost_src_pads()
        
        if self.have_video:
            self.source.create_ghost_src_pad(None,"video_preview1")
            self.source.create_ghost_src_pad(None,"video_preview2")
                
            self.preview_widget.create_ghost_sink_pads()
            self.preview_subwindow.create_ghost_sink_pads()
            
            self.preview_caps.create_ghost_sink_pads()
            self.preview_caps.create_ghost_src_pads()
            
            self.preview_caps.link_caps_elements()
    
        
        #LINK CONTAINERS ELEMENTS-------------------------------------------------------------------
        
        self.source_caps.link_caps_elements()
        
        
        #LINK CONTAINERS ---------------------------------------------------------------------------
        
        if self.source.have_video:
            
            #video caps string
            string_width = "width="+str(self.video_width)
            string_height = "height="+str(self.video_height)
            string_framerate = "framerate="+str(self.video_framerate)+"/1"
            
            if self.is_image:
                self.videocaps_string = "video/x-raw,"+string_framerate+",format="+Defaults.video_format
                
            else:
                self.videocaps_string = "video/x-raw,"+string_width+","+string_height+","+string_framerate+",format="+Defaults.video_format
            
            #Link containers
            self.source.link_containers("video_src", self.source_caps, "video_sink")
            self.source.link_containers("video_preview1", self.preview_caps, "video_sink")     
            self.preview_caps.link_containers("video_src", self.preview_widget, "video_sink")
            self.source.link_containers("video_preview2", self.preview_subwindow, "video_sink")
            
            self.source_caps.set_caps("videocaps", self.videocaps_string)
            self.preview_caps.set_caps("videocaps", self.videocaps_string)
            
            self.source_caps.set_properties()
            self.preview_caps.set_properties()
            
            self.preview_widget.set_sync(True, False)
            self.preview_subwindow.set_sync(True, False)
            
            self.preview_widget.set_state_playing()
            self.preview_subwindow.set_state_playing() 
            self.preview_caps.set_state_playing()
        
        
        if self.source.have_audio:
            self.audiocaps_string = "audio/x-raw, format=(string)F32LE, layout=(string)interleaved, rate=(int)44000, channels=(int)2"
            
            self.source.link_containers("audio_src", self.source_caps, "audio_sink")
            
            self.source_caps.set_caps("audiocaps", self.audiocaps_string)
            self.source_caps.set_property("volume", "volume", 1)
        
        #SET ELEMENTS PROPERTIES -------------------------------------------------------------------
        
        
        self.source.set_property("uridecodebin", "uri", self.the_uri)
        #self.source.set_property("filesrc", "location", self.the_uri)
        

        self.source_caps.block_pads(self.link_to_audiomixer,self.link_to_videomixer)

        self.source.set_state_playing()
        self.source_caps.set_state_playing()
         
        
        
    def blocked(self,pad,info,caps_container):
        string = pad.query_caps(None).to_string()
        if string.startswith('video/') and caps_container.have_video:
            self.source_caps.video_ready = True
            
        elif string.startswith('audio/') and caps_container.have_audio:
            self.source_caps.audio_ready = True
            
        if caps_container.audio_ready and caps_container.video_ready:
            self.mixer.link_to_videomixer(caps_container)
            self.mixer.link_to_audiomixer(caps_container)
            caps_container.unblock_videosink_pad()
            caps_container.unblock_audiosink_pad()
        

    def play(self):
        pass
        
    def stop(self):
        duration = self.source.the_bin.query_duration(Gst.Format.TIME)
        position = self.source.the_bin.query_position(Gst.Format.TIME)
        
        print("duration: ",duration)
        print("position: ",position)
        
        
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
        source_class.set_source_properties("File",self.the_uri,None)
        