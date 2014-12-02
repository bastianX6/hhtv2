'''
Created on 26-11-2013

@author: bastian
'''

from Containers.Container import Container

import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst

class RtmpSinkContainer(Container):
    '''
    classdocs
    '''


    def __init__(self,have_audio,have_video):
        '''
        Constructor
        '''
        super().__init__()
        
        self.pipeline = Gst.Pipeline()
        
        self.add_element("flvmux", "mux")
        self.add_element("rtmpsink", "rtmp")
            
        self.have_audio = have_audio
        self.have_video = have_video
        
        self.container_list = []
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect('message::error', self.__on_error)
        self.bus.connect('message', self.__message)
        
       
    def add_container_to_pipeline(self,container):
        self.container_list.append(container)
        self.pipeline.add(container.the_bin)
        
    def remove_container_from_pipeline(self,container):
        self.container_list.remove(container)
        self.pipeline.remove(container.the_bin)
        
    def play_pipeline(self):
        self.pipeline.set_state(Gst.State.PLAYING)
        
    def stop_pipeline(self):
        self.pipeline.send_event(Gst.Event.new_eos())
        self.pipeline.set_state(Gst.State.NULL)
        
    def pause_pipeline(self):
        self.pipeline.set_state(Gst.State.PAUSED)
        
    def create_ghost_sink_pads(self):
        if self.have_audio:
            self.__create_audio_ghost_sink_pad()
            
        if self.have_video:
            self.__create_video_ghost_sink_pad()
        
    def __create_audio_ghost_sink_pad(self):
        self.create_ghost_pad("audioqueue", "sink", False, "audio_sink")
        
    def __create_video_ghost_sink_pad(self):
        self.create_ghost_pad("videoqueue", "sink", False, "video_sink")
       
    def add_container_elements(self,audio_codec,video_codec):
        
        if self.have_audio:
            
            if audio_codec == "MP3":
                self.add_element("lamemp3enc", "audioenc")
                
            elif audio_codec == "AAC":
                self.add_element("faac", "audioenc")
            
            
            self.add_element("queue", "audioqueue")
            self.audio_codec = audio_codec
        
        if self.have_video:
            
            self.add_element("x264enc", "videoenc")
            
            self.add_element("queue", "videoqueue") 
            self.video_codec = video_codec
        
    def set_container_properties(self,audio_bitrate,video_bitrate,rtmp_location):
        
        if self.have_audio:
            
            if self.audio_codec == "MP3":
                self.set_property("audioenc", "target", 1)
                self.set_property("audioenc", "cbr", True)
                self.set_property("audioenc", "bitrate", audio_bitrate)
                
            elif self.audio_codec == "AAC":
                self.set_property("audioenc", "rate-control", 1)
                self.set_property("audioenc", "bitrate", audio_bitrate*1000)
                
                
        if self.have_video:
            
            if self.video_codec == "H264":
                self.set_property("videoenc", "tune", 0x00000004)
                self.set_property("videoenc", "bitrate", video_bitrate)
                
                
        self.rtmp_location = rtmp_location
        self.set_property("rtmp", "location", self.rtmp_location)
                
    
        
    #---------------------------------------------------
    
    def link_container_elements(self):
        self.link_elements("mux", "rtmp")
            
        if self.have_audio:
            self.__link_audio_elements()
            
        if self.have_video:
            self.__link_video_elements()
        
    def __link_audio_elements(self):
        self.link_elements("audioqueue", "audioenc")
        self.link_pads("audioenc", "src", "mux", "audio", False, True)
        
    def __link_video_elements(self):
        self.link_elements("videoqueue", "videoenc")
        self.link_pads("videoenc", "src", "mux", "video", False, True)
        
    def __on_error(self, bus, msg):
        print('on_error() - Rtmp:', msg.parse_error())
        
    def __message(self, bus, msg):
        print('-------------------------------------------')
        if msg.type == Gst.MessageType.STATE_CHANGED:
            states = msg.parse_state_changed()
            print('Old State',self.parse_state(states[0])," | New state: ",self.parse_state(states[1])," | State pending: ",self.parse_state(states[2]))
            
        if msg.type == Gst.MessageType.STREAM_STATUS:
            stream_status = msg.parse_stream_status()
            print('Stream Status:',stream_status[0])
            print('Element:',stream_status[1])
            
        if msg.type == Gst.MessageType.WARNING:
            warning = msg.parse_warning()
            print('Error:',warning[0])
            print('Details:',warning[1])
            
        if msg.type == Gst.MessageType.TAG:
            print('Tag:',msg.parse_tag().to_string())
            
        else:
            print("Message: ",msg.type)
            
        
        