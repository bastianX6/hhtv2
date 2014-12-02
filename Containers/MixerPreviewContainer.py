'''
Created on 10-10-2013

@author: bastian
'''

from Containers.Container import Container

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject,GdkX11, GstVideo

class MixerPreviewContainer(Container):
    '''
    classdocs
    '''


    def __init__(self,have_audio,have_video,mixer_bus,xid):
        '''
        Constructor
        '''
        super().__init__()
        
        self.have_audio = have_audio
        self.have_video = have_video
        self.xid = xid
        self.bus = mixer_bus
        self.bus.add_signal_watch()
        self.bus.enable_sync_message_emission()
        
        
        #ADD ELEMENTS
        
        if self.have_video:
            self.add_element("queue", "videoqueue")
            self.add_element("xvimagesink", "videosink")
            
            self.link_elements("videoqueue", "videosink")
            
            self.set_property("videosink", "sync", False)
            self.set_property("videosink", "qos", False)
        
            xvimagesink = self.element_list["videosink"]
        
            self.bus.connect('sync-message::element', self.__on_sync_message,self.xid,xvimagesink)
        
        if self.have_audio:
            self.add_element("queue", "audioqueue")
            self.add_element("audioconvert", "audioconvert")
            self.add_element("volume", "volume")
            self.add_element("alsasink", "audiosink")
            
            self.link_elements("audioqueue", "volume")
            self.link_elements("volume", "audioconvert")
            self.link_elements("audioconvert", "audiosink")
            
            self.set_property("audiosink", "sync", False)
        
    def __on_sync_message(self, bus, msg,win_id,videosink):
        if msg.get_structure().get_name() == 'prepare-window-handle':
            #print('prepare-window-handle')
            #print("win_id: "+str(win_id))
            videosink.set_window_handle(win_id)
        
        
    def create_ghost_sink_pads(self):
        if self.have_audio:
            self.create_ghost_pad("audioqueue", "sink", False, "audio_sink")
            
        if self.have_video:
            self.create_ghost_pad("videoqueue", "sink", False, "video_sink")
            
            
    def set_sync(self,audio_sync,video_sync):
        if self.have_audio:
            self.set_property("audiosink", "sync", audio_sync)
            
        if self.have_video:
            self.set_property("videosink", "sync", video_sync)
   

