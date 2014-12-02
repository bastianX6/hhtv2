'''
Created on 10-10-2013

@author: bastian
'''

from Containers.Container import Container

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject,GdkX11, GstVideo

class XVideoContainer(Container):
    '''
    classdocs
    '''


    def __init__(self,have_audio, have_video,host,port,xid,sync=True):
        '''
        Constructor
        '''
        super().__init__()
        
        self.have_audio = have_audio
        self.have_video = have_video
        self.xid = xid
        self.host = host
        self.port= port
        
        
        #create pipeline and get bus
        self.pipeline = Gst.Pipeline()
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        
        self.bus.enable_sync_message_emission()
        self.bus.connect('message::error', self.__on_error,self.port)
        self.bus.connect('sync-message::element', self.__on_sync_message,self.xid)
        self.bus.connect('message', self.__message,self.port)
        
        #add elements
        
        #tcp src
        self.add_element("tcpclientsrc", "tcpclientsrc")
        self.add_element("decodebin", "decodebin")
        
        
        #video elements
        if self.have_video:
            self.add_element("queue", "videoqueue")
            self.add_element("videoconvert", "videoconvert")
            self.add_element("autovideosink", "videosink")
        
        #audio elements 
        if self.have_audio:
            self.add_element("queue", "audioqueue")
            self.add_element("audioconvert", "audioconvert")
            self.add_element("volume", "volume")
            self.add_element("alsasink", "audiosink")
        
        
        self.pipeline.add(self.the_bin)
        
        #link elements
        
        self.link_elements("tcpclientsrc", "decodebin")
        decodebin = self.element_list["decodebin"]
        decodebin.connect("pad-added",self.__on_pad_added_decodebin)
        
        #video
        if self.have_video:
            self.link_elements("videoqueue", "videoconvert")
            self.link_elements("videoconvert", "videosink")
            
        if self.have_audio:
            self.link_elements("audioqueue", "volume")
            self.link_elements("volume", "audioconvert")
            self.link_elements("audioconvert", "audiosink")
        
        #set properties
        
        if self.have_video:
            #self.set_property("videosink", "async", False)
            self.set_property("videosink", "sync", sync)
        
        if self.have_audio:
            self.set_property("audiosink", "sync", False)
            
        self.set_property("tcpclientsrc", "host", self.host)
        self.set_property("tcpclientsrc", "port", self.port)
        
        #self.set_property("videosink", "double-buffer", True)
        
        
        
        
        
        
    def __on_sync_message(self, bus, msg,win_id):
        if msg.get_structure().get_name() == 'prepare-window-handle':
            print('prepare-window-handle')
            print("win_id: "+str(win_id))
            msg.src.set_window_handle(win_id)
            
    def __on_error(self, bus, msg,port):
        print('on_error():', msg.parse_error())
        print("port: "+str(port))
        
    def play_pipeline(self):
        self.pipeline.set_state(Gst.State.PLAYING)
        
    def pause_pipeline(self):
        self.pipeline.set_state(Gst.State.PAUSED)
        
    def stop_pipeline(self):
        self.pipeline.set_state(Gst.State.NULL)
        
    def __link_to_videoqueue(self,pad_src):
        #print("link to videoqueue")
        videoqueue = self.element_list["videoqueue"]            
        pad_videoqueue = videoqueue.get_static_pad("sink")
        pad_src.link(pad_videoqueue)
    
    def __link_to_audioqueue(self,pad_src):
        #print("link to audioqueue")
        audioqueue = self.element_list["audioqueue"]
        pad_audioqueue = audioqueue.get_static_pad("sink")
        pad_src.link(pad_audioqueue)
        
    def __on_pad_added_decodebin(self, element, pad):
        string = pad.query_caps(None).to_string()
        if string.startswith('video/') and self.have_video:
            self.__link_to_videoqueue(pad)
                        
        elif string.startswith('audio/') and self.have_audio:
            self.__link_to_audioqueue(pad)
            
            
    def __message(self, bus, msg,port):
        '''print('-------------------------------------------')
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
            
        else:
            print("Message: ",msg.type)
        
        
        print("port: "+str(port))'''
