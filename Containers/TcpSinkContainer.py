'''
Created on 26-11-2013

@author: bastian
'''

from Containers.Container import Container

import sys
import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst

class TcpSinkContainer(Container):
    '''
    classdocs
    '''


    def __init__(self,have_audio,have_video,host,port,sync_method=1,recover_policy=1):
        '''
        Constructor
        '''
        super().__init__()
        
        self.have_audio = have_audio
        self.have_video = have_video 
        self.host = host
        self.port = port
        self.sync_method = sync_method
        self.recover_policy = recover_policy
        
        self.pipeline = Gst.Pipeline()
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        
        self.bus.enable_sync_message_emission()
        self.bus.connect('message::error', self.__on_error,self.port)
        self.bus.connect('message', self.__message,self.port)
        
        self.add_element("matroskamux", "mux")
        self.add_element("tcpserversink", "tcp")
        
        if have_audio:
            self.add_element("vorbisenc", "audioenc")
            self.add_element("queue", "audioqueue")
        if have_video:
            self.add_element("x264enc", "videoenc")
            self.add_element("queue", "videoqueue")
            self.set_property("videoenc", "tune", 0x00000004)
            self.set_property("videoenc", "bitrate", 3000)
            
        
        
        self.container_list = []
        
        tcpserversink = self.element_list["tcp"]
        tcpserversink.connect("client-added",self.__client_added,self.port)
        
    def add_container_to_pipeline(self,container):
        self.container_list.append(container)
        self.pipeline.add(container.the_bin)
        
    def remove_container_from_pipeline(self,container):
        self.container_list.remove(container)
        self.pipeline.remove(container.the_bin)
        
    def play_pipeline(self):
        self.pipeline.set_state(Gst.State.PLAYING)
        
    def stop_pipeline(self):
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
        
    #---------------------------------------------------
    
    def link_tcp_elements(self):
        self.link_elements("mux", "tcp")
            
        if self.have_audio:
            self.__link_audio_elements()
            
        if self.have_video:
            self.__link_video_elements()
        
    def __link_audio_elements(self):
        self.link_elements("audioqueue", "audioenc")
        self.link_pads("audioenc", "src", "mux", "audio_%u", False, True)
        
    def __link_video_elements(self):
        self.link_elements("videoqueue", "videoenc")
        self.link_pads("videoenc", "src", "mux", "video_%u", False, True)
        
    def set_tcp_properties(self):
        self.set_property("tcp", "host", self.host)
        self.set_property("tcp", "port", self.port)
        self.set_property("tcp", "sync-method", self.sync_method)
        self.set_property("tcp", "recover-policy", self.recover_policy)
        self.set_property("tcp", "recover-policy", self.recover_policy)
        
    '''def set_tcp_properties_2(self,sync,async):
        self.set_property("tcp", "host", self.host)
        self.set_property("tcp", "port", self.port)
        self.set_property("tcp", "sync-method", self.sync_method)
        self.set_property("tcp", "recover-policy", self.recover_policy)
        self.set_property("tcp", "async", async)
        self.set_property("tcp", "sync", sync)'''
        
    def __client_added(self,obj,arg0,user_data):
        print("TCP Server Sink - client-added")
        print("Port: "+str(user_data))
        
        
        
    def connect_message_eos(self,function):
        self.bus.connect('message::eos', function,self.port)
        
    def __on_error(self, bus, msg,port):
        print('on_error():', msg.parse_error())
        print("port: "+str(port))
        
    def __on_eos(self, bus, msg,port):
        print('on_eos():')
        print("port: "+str(port))
        
    def __message(self, bus, msg,port):
        '''print('-------------------------------------------')
        if msg.type == Gst.MessageType.STATE_CHANGED:
            states = msg.parse_state_changed()
            print('Old State',self.parse_state(states[0])," | New state: ",self.parse_state(states[1])," | State pending: ",self.parse_state(states[2]))
            
        if msg.type == Gst.MessageType.STREAM_STATUS:
            stream_status = msg.parse_stream_status()
            print('Stream Status:',stream_status[0])
            print('Element:',stream_status[0])
        
        
        print("port: "+str(port))'''
        