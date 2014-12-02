'''
Created on 06-10-2013

@author: bastian
'''

from Containers.Container import Container

import sys
import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst

class FileSrcContainer(Container):
    '''
    classdocs
    '''


    def __init__(self,have_audio,have_video,have_uri = True):
        '''
        Constructor
        '''
        
        super().__init__()
        
        
        
        if have_video:
            self.add_element("videoconvert", "videoconvert")
            self.add_element("tee", "videotee")
            
        if have_audio:
            self.add_element("audioconvert", "audioconvert")
            self.add_element("tee", "audiotee")
        
        
        self.add_element("multifilesrc", "filesrc")
        self.add_element("decodebin", "decodebin")
        
        self.link_elements("filesrc", "decodebin")
        self.set_property("filesrc", "loop", True)
        decodebin = self.element_list["decodebin"]
            
        decodebin.connect("pad-added", self.__on_pad_added_decodebin)
        
        
        self.have_video = have_video
        self.have_audio = have_audio
        self.have_uri = have_uri
        
        
    def __link_to_videoconvert(self,pad_src):
        #print("link to videoconvert")
        videoconvert = self.element_list["videoconvert"]
            
        pad_videoconvert = videoconvert.get_static_pad("sink")
        pad_src.link(pad_videoconvert)
        self.link_elements("videoconvert", "videotee") 
        
    
    def __link_to_audioconvert(self,pad_src):
        #print("link to audioconvert")
        audioconvert = self.element_list["audioconvert"]
        pad_audioconvert = audioconvert.get_static_pad("sink")
        pad_src.link(pad_audioconvert)
        self.link_elements("audioconvert", "audiotee")
        
    def __on_pad_added_decodebin(self, element, pad):
        string = pad.query_caps(None).to_string()
        #print("string: "+string)
        if string.startswith('video/') and self.have_video:
            self.__link_to_videoconvert(pad)
                
        elif string.startswith('audio/') and self.have_audio:
            self.__link_to_audioconvert(pad)
        
    def create_ghost_src_pad(self,audio_pad_name="audio_src",video_pad_name="video_src"):
        if self.have_video:
            self.__make_video_ghost_pad(video_pad_name)
            
        if self.have_audio:
            self.__make_audio_ghost_pad(audio_pad_name)
        
    def __make_audio_ghost_pad(self,pad_name):

        self.create_ghost_pad("audiotee", "src_%u", True, pad_name)
        
    def __make_video_ghost_pad(self,pad_name):
        self.create_ghost_pad("videotee", "src_%u", True, pad_name)
        
    '''def block_events(self):
        filesrc = self.element_list["filesrc"]
        pad = filesrc.get_static_pad("src")
        pad.add_probe(Gst.PadProbeType.EVENT_BOTH ,self.blocked,0)
        
    def blocked(self,arg1,arg2,arg3):
        print("blocked: ")
        print("arg1: ",arg1," \nCaps: ",arg1.query_caps(None).to_string())
        
        print("arg2: ",arg2)
        print("arg3: ",arg3)'''