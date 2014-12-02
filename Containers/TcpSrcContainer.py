'''
Created on 26-11-2013

@author: bastian
'''
from Containers.Container import Container

import sys
import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst


class TcpSrcContainer(Container):
    '''
    classdocs
    '''


    def __init__(self,have_audio,have_video,host,port):
        '''
        Constructor
        '''
        super().__init__()
        
        self.have_audio = have_audio
        self.have_video = have_video
        self.host = host
        self.port = port
        self.no_more_pads = False
        
        self.add_element("tcpclientsrc", "tcp_src")
        self.add_element("decodebin", "decodebin")
        
        if have_audio:
            self.add_element("audioconvert", "audioconvert")
            self.__block_audioconvert_pad()
        
        if have_video:
            self.add_element("videoconvert", "videoconvert")
            self.__block_videoconvert_pad()

        
            
        decodebin = self.element_list["decodebin"]
            
        decodebin.connect("pad-added", self.__on_pad_added_decodebin)
        decodebin.connect("no-more-pads", self.__no_more_pads)
        
        
        
        
        
    def __link_to_videoconvert(self,pad_src):
        #print("link to videoconvert")
        videoconvert = self.element_list["videoconvert"]
            
        pad_videoconvert = videoconvert.get_static_pad("sink")
        linked = pad_src.link(pad_videoconvert)
        
        #print("TcpSrcContainer - link_to_videoconvert")
        #print("linked: "+str(linked))
        
    
    def __link_to_audioconvert(self,pad_src):
        #print("link to audioconvert")
        audioconvert = self.element_list["audioconvert"]
        pad_audioconvert = audioconvert.get_static_pad("sink")
        linked = pad_src.link(pad_audioconvert)
        
        #print("TcpSrcContainer - link_to_audioconvert")
        #print("linked: "+str(linked))
        
    def __on_pad_added_decodebin(self, element, pad):
        string = pad.query_caps(None).to_string()
        #print("string: "+string)
        if string.startswith('video/') and self.have_video:
            self.__link_to_videoconvert(pad)
                
        elif string.startswith('audio/') and self.have_audio:
            self.__link_to_audioconvert(pad)
            
            
    def create_ghost_src_pad(self):
        if self.have_video:
            self.__make_video_ghost_pad()
            
        if self.have_audio:
            self.__make_audio_ghost_pad()
        
    def __make_audio_ghost_pad(self):
        self.create_ghost_pad("audioconvert", "src", False, "audio_src")
        
    def __make_video_ghost_pad(self):
        self.create_ghost_pad("videoconvert", "src", False, "video_src")
        
    def set_properties(self):
        self.set_property("tcp_src", "host", self.host)
        self.set_property("tcp_src", "port", self.port)
        self.set_property("tcp_src", "do-timestamp", True)
        
    def link_container_elements(self):
        self.link_elements("tcp_src", "decodebin")
        
    def __no_more_pads(self,element):
        self.no_more_pads = True
        print("No more pads!!")
        
    def __block_videoconvert_pad(self):
        #print("block videoconvert pad")
        videoconvert = self.element_list["videoconvert"]
        src_pad = self.get_pad(videoconvert, "src", False)
        self.videoconvert_id =  src_pad.add_probe(Gst.PadProbeType.BLOCK_DOWNSTREAM,self.__unblock_videoconvert_pad,"hola")
    
    def __block_audioconvert_pad(self):
        #print("block audioconvert pad")
        audioconvert = self.element_list["audioconvert"]
        src_pad = self.get_pad(audioconvert, "src", False)
        self.audioconvert_id =  src_pad.add_probe(Gst.PadProbeType.BLOCK_DOWNSTREAM,self.__unblock_audioconvert_pad,"hola")
    
    def __unblock_videoconvert_pad(self,pad,info,user_data):
        if self.no_more_pads:
            pad.remove_probe(self.videoconvert_id)
        
    def __unblock_audioconvert_pad(self,pad,info,user_data):
        if self.no_more_pads:
            pad.remove_probe(self.audioconvert_id)