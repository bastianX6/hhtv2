'''
Created on 08-10-2013

@author: bastian
'''

from Containers.Container import Container

import sys
import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst

class CapsContainer(Container):
    '''
    classdocs
    '''


    def __init__(self,have_audio,have_video,is_a_image = False):
        '''
        Constructor
        '''
        super().__init__()
        
        if have_audio:
            
            self.add_element("queue", "audioqueue")
            self.add_element("capsfilter", "audiocaps")
            self.add_element("audiorate", "audiorate")
            self.add_element("audioresample", "audioresample")
            self.add_element("volume", "volume")
            self.audio_ready = False
            
            
        if have_video:
            self.add_element("queue", "videoqueue")
            self.add_element("textoverlay", "textoverlay")
            self.add_element("capsfilter", "videocaps")
            self.add_element("videoscale", "videoscale")
            self.set_property("videoscale", "add-borders", False)
            self.video_ready = False
            
            if is_a_image:
                self.add_element("imagefreeze", "imagefreeze")
                
            else:
                self.add_element("videorate", "videorate")
            
            
            
        
        self.have_audio = have_audio
        self.have_video = have_video 
        self.is_a_image = is_a_image
            
        
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
        
    def create_ghost_src_pads(self):
        if self.have_audio:
            self.__create_audio_ghost_src_pad()
            
        if self.have_video:
            self.__create_video_ghost_src_pad()
            
    def __create_audio_ghost_src_pad(self):
        self.create_ghost_pad("audiocaps", "src", False, "audio_src")
        
    def __create_video_ghost_src_pad(self):
        self.create_ghost_pad("videocaps", "src", False, "video_src")
        
        
    #---------------------------------------------------
    
    def link_caps_elements(self):
        if self.have_audio:
            self.__link_audio_elements()
            
        if self.have_video:
            self.__link_video_elements()
        
    def __link_audio_elements(self):
        
        self.link_elements("audioqueue", "audioresample")
        self.link_elements("audioresample","audiorate")
        self.link_elements("audiorate","volume")
        
        
        self.link_elements("volume","audiocaps")
        
    def __link_video_elements(self):
        
        
        if self.is_a_image:
            self.link_elements("videoqueue", "imagefreeze")
            self.link_elements("imagefreeze","videoscale")
            self.link_elements("videoscale","textoverlay")
            self.link_elements("textoverlay","videocaps")
            
        else:
            self.link_elements("videoqueue", "videorate")
            self.link_elements("videorate","videoscale")
            self.link_elements("videoscale","textoverlay")
            self.link_elements("textoverlay","videocaps")
    
    def block_pads(self,audio_callback,video_callback):
        
        if self.have_audio:
            self.block_audiosink_bin_pad(audio_callback)
            
        if self.have_video:
            self.block_videosink_bin_pad(video_callback)
            
            
    def unblock_pads(self):
        if self.have_audio:
            self.unblock_audiosink_pad()
            
        if self.have_video:
            self.unblock_videosink_pad()
    
    def block_videosink_bin_pad(self,function):
        pad = self.get_bin_pad("video_sink")
        self.videosink_pad_id = pad.add_probe(Gst.PadProbeType.BLOCK_DOWNSTREAM,function,self)
        
    def block_audiosink_bin_pad(self,function):
        pad = self.get_bin_pad("audio_sink")
        self.audiosink_pad_id = pad.add_probe(Gst.PadProbeType.BLOCK_DOWNSTREAM ,function,self)
        
    def unblock_videosink_pad(self):
        pad = self.get_bin_pad("video_sink")
        pad.remove_probe(self.videosink_pad_id)
        
    def unblock_audiosink_pad(self):
        pad = self.get_bin_pad("audio_sink")
        pad.remove_probe(self.audiosink_pad_id)
        
    def audio_blocked(self,pad,info,user_data):
        print("audio blocked")
    
    def video_blocked(self,pad,info,user_data):
        print("video blocked")
    
    
    def set_properties(self):
        
        if self.have_video:
            #self.set_property("alpha", "alpha", 1)
            self.set_property("textoverlay", "text", "")
            self.set_property("textoverlay", "halignment", 4)
            self.set_property("textoverlay", "valignment", 3)
            self.set_property("videoscale", "method", 0)
        if self.have_audio:
            pass
        #self.set_property("alpha", "method", 1)